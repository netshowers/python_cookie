"""
爬取的是某东的8424西瓜的商品信息
要爬取企业信息需要验证码，要一个一个输入
若不爬取企业信息则可以实现自动爬取想要的页数，请做如下改动
注释掉97行115行124行132行   打开125行（加了几行注释可能行数就变了，不过下面相应的行也会标出注释）
"""
import re
import requests
# import xlwt
from openpyxl import Workbook
from PIL import Image
from bs4 import BeautifulSoup
# from lxml import etree

item_value = []
count = 1
browser = requests.session()
requestVerifyCodeUrl = "https://mall.jd.com/sys/vc/createVerifyCode.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


def parserUrl(url, params={}):
    # 解析URL(要多次请求所以就单独列出来一个方法)
    global headers
    req = requests.get(url, headers=headers, params=params)  # headers一定要有，模拟浏览器请求，params是参数
    # time.sleep(1)  #貌似不需要1s就可以一直请求某东，某宝好像就会有验证
    soup = BeautifulSoup(req.text, "lxml")
    return soup


def enterprisePage(url):
    # 处理企业详情页面相关数据
    while True:
        global headers
        global requestVerifyCodeUrl
        # 这里不可以用requests.get请求了，因为cookie的缘故，这个是我找到的最简单的解决办法了browser = requests.session()就可以自动保存cookie了
        req = browser.get(requestVerifyCodeUrl, headers=headers)
        # 保存验证码图片
        f = open("VerifyCodeImage.jpg", 'wb')
        f.write(req.content)
        f.close()
        f1 = open("VerifyCodeImage.jpg", 'rb')
        image = Image.open(f1)
        image.show()
        f1.close()
        # 手动输入
        vc = input('请输入验证码:')  # 深度学习识别会在后续的文章中给出
        datas = {'verifyCode': vc}
        # 这里使用browser.post就会和上面请求验证码的cookie一致了
        req2 = browser.post(url, data=datas, headers=headers)
        soup = BeautifulSoup(req2.text, "lxml")
        # 判断若是有form的代码块则证明没有验证成功，这个就要去网页源码中观察俩个页面的差异了
        if soup.find('form'):
            print('验证码输入错误！请重新输入！')
            continue
        infoList = soup.find_all('li', attrs={'class': 'noBorder'})  # 获取企业相关信息代码段
        for info in infoList:
            if info.find('label', attrs={'class': 'jLabel'}):
                if info.find('label', attrs={'class': 'jLabel'}).text == "企业名称： ":
                    item_value.append(info.find('span').text)  # 企业名称
                if info.find('label', attrs={'class': 'jLabel'}).text == "公司地址：":
                    item_value.append(info.find('span').text)  # 企业地址
        return


def itemPage(url):
    # 处理商品详情页面相关数据
    # 净含量是在列表页面没有的所以要进到详情页面获取
    soup = parserUrl(url)
    clearfixList = soup.find_all('dl', attrs={'class': 'clearfix'})  # 获取重量相关代码段
    for clearfix in clearfixList:
        if clearfix.find('dt').text == "净含量":
            weight = re.sub("[a-zA-Z]", "", clearfix.find('dd').text)
            return weight
    return None


def storePage(url):
    # 处理店铺详情页面相关数据
    # 严格来说并没有进到店铺页面，这个页面没有什么要获取的，但是要从这里获取企业页面于是就中间加了这么一个函数
    storID = re.sub("[^0-9]", "", url)
    enterpriseUrl = 'https://mall.jd.com/showLicence-' + str(storID) + '.html'
    # 本来企业url是在店铺页面中爬取的，但是是动态加载的，源码中是没有的，但是经过观察发现这这两个页面的url一部分是固定的，
    # 只是更改了店铺的id，这样我们就可以拼接出企业url了（曲线救国）
    enterprisePage(enterpriseUrl)


def mainPage(sheet, n, kw):
    # 处理搜索页面相关数据
    url = "https://search.jd.com/search?"
    # 只要参数这样设置只改变n就可以爬取想要的页数的数据了，不用考虑翻页和下拉滚动条
    params = {"keyword": kw, 'page': str(n), 'scrolling': 'y'}
    soup = parserUrl(url, params)
    # 下面的相关信息的获取都是要求网页源码中对应的字段去匹配，并不是所有网站通用的
    item_list = soup.find_all("li", attrs={"class": "gl-item"})
    for item in item_list:
        # p_name = item.find('div', attrs={"class": "p-name p-name-type-2"})  # 获取商品相关代码段
        p_name = item.find('div', attrs={"class": "p-name"})  # 获取图书类商品相关代码段
        if p_name is not None:
            itemName = p_name.find('em').text
            itemUrl = 'https:' + p_name.find('a')['href']
            p_price = item.find('div', attrs={"class": "p-price"})  # 获取价格相关代码段
            itemPrice = p_price.find('i').text
            # p_shop = item.find('div', attrs={"class": "p-shop"})  # 获取店铺相关代码段
            # p_shop = item.find('div', attrs={"class": "p-shop"})  # 获取图书类店铺相关代码段
            # if(p_shop is not None):
            #     a_elem = p_shop.find('a')
            #     if a_elem is not None:
            #         storeName = a_elem.text
            #         storeUrl = 'https:' + a_elem['href']
            # else:
            #     p_shop = item.find('div', attrs={"class": "p-shopnum"})
            #     if (p_shop is not None):
            #         a_elem = p_shop.find('a')
            #         if a_elem is not None:
            #             storeName = a_elem.text
            #             storeUrl = 'https:' + a_elem['href']

            p_shop = item.find('div', attrs={"class": "p-shop"}) or item.find('div', attrs={
                "class": "p-shopnum"})  # 获取图书类店铺相关代码段
            storeName = ''
            storeUrl = ''
            if p_shop is not None:
                a_elem = p_shop.find('a')
                if a_elem is not None:
                    storeName = a_elem.text
                    storeUrl = f"https:{a_elem.get('href', '')}"  # 使用get()方法和f-string
            item_value.clear()
            item_value.append(storeName)  # 店铺名字
            item_value.append(storeUrl)  # 店铺URL
            item_value.append(itemName)  # 商品名字
            item_value.append(itemUrl)  # 商品URl
            # storePage(storeUrl)  # 在店铺页面处理数据   不输入验证码注释掉这一行
            item_value.append(itemPrice)  # 商品价格
            itemWeight = itemPage(itemUrl)  # 在商品页面处理数据
            if itemWeight:
                item_value.append(itemWeight)  # 商品重量
            else:
                item_value.append(0)
            if itemWeight:
                itemUnitPrice = float(itemPrice) / float(itemWeight) / 2
                item_value.append('%.2f' % itemUnitPrice)  # 商品单价
            else:
                item_value.append(0)

            # 写入excel表
            # global count
            # for i in range(0, len(item_value)):
            # sheet.write(count, i, item_value[i])
            # sheet.append(item_value[i])# xlsx写入数据
            # count += 1
            # if count == 4: return  # 不输入验证码注释掉这一行，数字减一是爬取商品的数目

            item = [storeName, storeUrl, itemName, itemUrl, itemPrice, itemWeight]
            print(item)
            sheet.append(item)

    if n % 2 == 0:
        print("******已完成第" + str(int(n / 2)) + "页商品信息写入******")


def main():
    kw = input("请输入要爬取的关键字: ")
    n = input("请输入要爬取的页数：")
    n = int(n) * 2
    print("**************正在写入**************")
    print("请稍候...")
    # value_title = ['店铺名称', '店铺URL', '商品名称', '商品URL', '企业名称', '企业地址', '价格(元)', '重量(kg)',
    #               '单价(元/500g)']  # 不输入验证码注释掉这一行并且打开下一行
    value_title = ['店铺名称', '店铺URL', '商品名称', '商品URL', '价格(元)', '重量(kg)', '单价(元/500g)']
    # workbook = xlwt.Workbook()
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(value_title)
    # sheet = workbook.add_sheet(kw)
    # for i in range(0, len(value_title)):
        # sheet.write(0, i, value_title[i])  # 写入表头
    #    sheet.append(value_title)  # xlsx写入表头
    '''    
    这里要说明一下某东的搜索页面最开始是只加载一半的，当下拉滚动条会加载剩下的一半，又发现url中的参数page=1当点击下一页page=3，
    会这样每次+2，通过下拉滚动条加载后半页抓包可见页面是发送了一个请求的，这个请求的网址的page参数是2，4，6双数的，
    不难发现只要n++就可以一个不漏的爬取所有信息了，不需要什么模拟下拉滚动条和翻页，所以要爬取1页page=1-2，爬取2页page=1-4，爬取3页page=1-6，
    不要习惯的从0开始哈
    '''
    for i in range(1, n + 1):
        mainPage(sheet, i, kw)
        # break  # 不输入验证码注释掉这一行
    workbook.save('D:/Document/Python/某东{}商品数据.xlsx'.format(kw))
    print("**************写入完成**************")


if __name__ == '__main__':
    main()

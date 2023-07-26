import time
import pandas as pd
import requests
# import xlwt
from lxml import etree
import urllib.parse

# from lxml import etree

item_list = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


def process():
    # Make a single request to fetch all the pages
    url = "https://www.juzikong.com/authors/87c50259-8e62-4868-ba5f-d20f4d67da67?page="
    base_url = "https://www.juzikong.com"

    for i in range(1, 11):
        page_url = url + str(i)
        result = requests.get(page_url, headers=headers).content.decode()
        html = etree.HTML(result)
        # div_list = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2][@class="list_s2gkX"]')
        div_list = html.xpath(".//div[contains(@class,'list')]/section")
        # print(div_list)
        for section in div_list:
            # print(etree.tostring(section, encoding="utf-8").decode())
            relative_url = section.xpath(".//div[contains(@class,'content')]/a/@href")[0]
            nickname = section.xpath(".//a[contains(@class,'nickname')]/text()")[0].strip()
            content = section.xpath(".//div[contains(@class,'content')]//span/text()")[0]
            full_url = urllib.parse.urljoin(base_url, relative_url)
            comment_count = section.xpath(".//a[contains(@class,'comment')]/span/text()")[0]
            like_count = section.xpath(".//span[contains(@class,'like')]/span/text()")[0]
            item = {'name': nickname, 'content': content, 'source': full_url, 'comment': comment_count,
                    'like': like_count}
            item_list.append(item)
        print("正在爬取第{}页".format(i))
        time.sleep(0.1)
    df = pd.DataFrame(item_list)
    # df.to_csv('D:/Document/Python/{}经典语录.csv'.format('模仿鲁迅'), encoding='utf_8_sig')
    df.to_excel('D:/Document/Python/{}经典语录.xlsx'.format('模仿鲁迅'), index=False)


def main():
    process()


if __name__ == '__main__':
    main()

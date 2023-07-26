# 导入模块
import json
import pandas
import requests


def main():
    # 创建空字典
    data = {
        "productColor": [],
        "nickname": [],
        "productSize": [],
        "content": []
    }

    # 循环换页
    for page in range(2):
        # 请求地址
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId" \
              "=100034710036&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(page)
        # 发送请求
        resp = requests.get(url)
        # json解码
        result = json.loads(resp.text[20:-2])["comments"]
        # 循环输出改为存入data字典
        for coment in result:
            # print("颜色:{},名字：{},内存:{},评论：{}".format(coment["productColor"],coment["nickname"],coment["productSize"],coment["content"]))
            # 颜色
            data['productColor'].append(coment["productColor"])
            # 名字
            data['nickname'].append(coment["nickname"])
            # 内存
            data['productSize'].append(coment["productSize"])
            # 评论
            data['content'].append(coment["content"])

    # print(data)

    # 将数据转换为DF类型
    df_response = pandas.DataFrame(data)

    # 直接to_excel
    df_response.to_excel('D:/document/mobile_less.xlsx', index=False)


if __name__ == '__main__':
    main()

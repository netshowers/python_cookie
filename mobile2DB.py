import json
# import pandas as pd
import requests
import psycopg2
import uuid


def main():
    # 创建空DataFrame
    # data = pd.DataFrame(columns=["productColor", "nickname", "productSize", "content"])
    # 建立数据库连接和游标对象
    db, cur = conn()
    # 循环换页
    for page in range(2):
        # 请求地址
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100034710036&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(
            page)
        # 发送请求
        resp = requests.get(url)
        # json解码
        ls = json.loads(resp.text[20:-2])["comments"]
        for comment in ls:
            # 颜色
            color = comment["productColor"]
            # 名字
            name = comment["nickname"]
            # 内存
            size = comment["productSize"]
            # 评论
            content = comment["content"]
            # 将数据添加到DataFrame data = data.append({"productColor": color, "nickname": name, "productSize": size,
            # "content": content}, ignore_index=True) 执行插入操作
            insert(cur, color, name, size, content)
    # 提交事务
    db.commit()
    # 关闭游标和连接
    cur.close()
    db.close()
    # 打印DataFrame
    # print(data)


def conn():
    # 建立数据库连接
    db = psycopg2.connect(
        host="192.168.126.82",
        port="5432",
        database="TNTLive230314",
        user="dbadmin",
        password="dl123"
    )
    # 创建游标对象
    cur = db.cursor()
    return db, cur


def insert(cur, color, name, size, content):
    # 生成UUID
    uuid_value = uuid.uuid1()
    # 准备INSERT INTO语句
    prepare_stmt = "INSERT INTO temp.mobile (id, color, name, size, content) VALUES (%s,%s,%s,%s,%s)"
    # 绑定参数并执行准备好的语句
    cur.execute(prepare_stmt, (str(uuid_value), color, name, size, content))


if __name__ == '__main__':
    main()

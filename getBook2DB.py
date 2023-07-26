# 导入模块
import json
import pandas
import requests
import psycopg2


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
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100034710036&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(
            page)
        # 发送请求
        resp = requests.get(url)
        # json解码
        ls = json.loads(resp.text[20:-2])["comments"]
        # 循环输出改为存入data字典
        # 创建游标对象
        db = conn()
        cur = db.cursor()
        for coment in ls:
            # print("颜色:{},名字：{},内存:{},评论：{}".format(coment["productColor"],coment["nickname"],coment["productSize"],coment["content"]))
            # 颜色
            color = coment["productColor"]
            # 名字
            name = coment["nickname"]
            # 内存
            size = coment["productSize"]
            # 评论
            content = coment["content"]
            insert(cur, color, name, size, content)
            # 提交事务
            db.commit()
        # 关闭游标和连接
        cur.close()
        db.close()
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
    return db


def insert(cur, color, name, size, content):
    # 执行SQL查询
    # cur.execute("select * from scm.plant")
    # 获取查询结果
    # rows = cur.fetchall()
    # 打印结果
    # for row in rows:
    #    print(row)
    # 准备INSERT INTO语句
    prepare_stmt = "INSERT INTO temp.mobile (id, color, name, size, content) VALUES (uuid_generate_v1(),%s,%s,%s,%s,%s)"
    # 执行准备语句
    # cur.execute(prepare_stmt)
    # 绑定参数并执行准备好的语句
    cur.execute(prepare_stmt, (color, name, size, content))


if __name__ == '__main__':
    main()

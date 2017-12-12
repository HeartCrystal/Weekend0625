import pymysql # 第三方的代码库,需要下载

def connDb():
    # 我们要想使用数据库, 需要知道数据库的哪些信息:
    # 至少要知道 用户名 和 密 码
    # 还有 服务器地址  和 端口号  数据库名  和 数据库的编码方式
    try:
        conn = pymysql.Connect(host="127.0.0.1", user="root", password="root", database="pirate", port=3306, charset='utf8')
        # 通过倒叙, 把最后一条数据放在最上面
        sql = "select * from hd_user ORDER BY id DESC"
        # 要想在代码中执行sql语句, 首先要获得数据库的游标cursor
        curs = conn.cursor()
        # 执行sql语句
        curs.execute(sql)
        # 获取数据库中返回的结果
        # result = curs.fetchall() # 获取所有返回结果
        result = curs.fetchone() # 获取第一条数据
        return result
    # 默认情况, 发生异常时, 后面的语句都不执行, 和断言一样
    finally:    # finally保证当发生异常时, 下面的语句仍然可以执行
        # 更详细的解释在QQ群, 读取txt文件的代码里
        curs.close()
        conn.close()

if __name__ == '__main__':
    result = connDb()
    for row in result:
        print(row)

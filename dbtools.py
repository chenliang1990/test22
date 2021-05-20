# 导入pymysql
import pymysql


# 1.数据库查询select
# FBIWARNING: 这些代码都是固定
def query(sql):
    """
        数据查询，只支持select，不支持update delete insert
        - 参数: sql- eg: "select * from t_user where id=123"
    """
    # 1.连接数据库
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    # db = pymysql.connect(host="127.0.0.1", user="ljtest", password="123456", db="ljtestdb")
    # 2.获取游标：查询窗口
    cur = db.cursor()
    # 3.执行sql语句
    cur.execute(sql)
    # 4.收集结果
    res = cur.fetchall()
    db.close()
    return res

def commit(sql):
    """
        修改方法，不支持select，只支持update delete insert
        - 参数: sql- eg: "update /delete /insert"
    """
    # 1.连接数据库
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    # 2.获取游标：查询窗口
    cur = db.cursor()
    # 3.执行sql语句
    cur.execute(sql)
    # 4.提交修改（事务）
    db.commit()
    db.close()

# sql = "update t_pymysql_account set password='12345678' where id=5"
# commit(sql)
# sql是字符串
# sql语句就是之前所学的sql
# sql = "select * from t_pymysql_account"
# res = query(sql)
# print(len(res))



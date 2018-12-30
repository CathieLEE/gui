import pymssql

# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
server='172.20.83.201:6164'
user='editor'
password='123456'
database='journal'
print('123')
conn = pymssql.connect(server, user, password, database)
print('123')
cursor = conn.cursor()

# 新建、插入操作
cursor.execute("""
SELECT JNO
FROM catelog
)
""")

conn.commit()


row = cursor.fetchone()


# 也可以使用for循环来迭代查询结果
# for row in cursor:
#     print("ID=%d, Name=%s" % (row[0], row[1]))

# 关闭连接
conn.close()
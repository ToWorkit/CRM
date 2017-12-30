import pymysql
# 连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="list", charset="utf8")
# 创建游标
cursor = conn.cursor()

# 正规写法
# cursor.execute('select username, password from userinfo where username=%s and password=%s', ('a', 123))
# result = cursor.fetchone()
# print(result)

# 易注入写法
sql = 'select username, password from userinfo where username="%s" and password="%s"'
# 密码不对，注入写法 or 1=1 忽略前面的 1=1 为true
# sql = sql % ('a" or 1=1 -- ', 1235445)
# sql 语句中 -- 为注释操作
sql = sql % ('a" -- ', 1235445)
cursor.execute(sql)
result = cursor.fetchone()
print(result)


# 关闭游标
cursor.close()
# 关闭连接
conn.close()

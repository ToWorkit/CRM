import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='list', charset='utf8')
# 创建游标
cursor = conn.cursor()

# sql语句
cursor.execute('insert into class(caption) values("三年七班")')
# 执行
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

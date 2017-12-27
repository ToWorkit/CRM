import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='list', charset='utf8')
# 创建游标
# cursor = conn.cursor()

# 游标参数（设置值为字典） -> 观察fetch系列的值
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# inp = input('请输入班级')
# sql语句
# 不要使用sql拼接，防止sql注入，要以参数的方式传递
# cursor.execute('insert into student(gender, class_id, sname) values(%s, %s, %s)', ('女', 1, '小夏')) 插入

lis = [
  ('男', 2, '小_01'),
  ('男', 2, '小_02'),
  ('女', 2, '小_03'),
]
# cursor.executemany('insert into student(gender, class_id, sname) values(%s, %s, %s)', lis) 插入列表(多条同时插入)

# cursor.execute('update student set sname=%s where sid=%s', ('小小', 3)) 更新

# cursor.execute('delete from score where sid=%s', (2, )) 删除

# 执行
# conn.commit()

# 查 -> 查不需要commit() 
# 数据为一时，fetchall => (一条数据), fetchone => 一条数据, fetchmany
# 已经将数据全部存储在内存里了，下面的取数据都是在操作内存中的数据
# r = cursor.execute('select * from student')

# 游标传入参数后自定义key
r = cursor.execute('select sname as s_n, sid, gender from student')

# 返回受影响的条数
print(r)
# 取数据
# result = cursor.fetchall() 所有
# print(result)

# result = cursor.fetchone() 第一个
# print(result)

# 指定条数
# result = cursor.fetchmany(3) 
# print(result)

# 获取最后一条的自增id
# r_2 = cursor.execute('insert into class(caption) values(%s)', ('国中三年'))
# 插入多条数据
r_2 = cursor.executemany('insert into class(caption) values(%s)', [('二年一班'), ('二年二班'), ('二年三班')])
conn.commit()
# 获取最后一条的id
nid = cursor.lastrowid
print(nid)

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

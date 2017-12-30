# -*- coding: utf-8 -*-

# 当前登录用户的权限列表
current_user_permission_list = []

# 当前登录用户的基本信息
# {'nid':1,'username': 'root', 'role_id': 1}
# role_id -> 权限id
current_user_info = {}

# 数据库连接
PY_MYSQL_CONN_DICT = {
  'host': '127.0.0.1',
  'port': 3306,
  'user': 'root',
  'passwd': 'root',
  'db': 'authdb',
  'charset': 'utf8'
}

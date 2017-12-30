# -*- coding:utf-8 -*-

from src.utils.db_connection import DbConnection

# 权限表
class PermissionRepository:
  def __init__(self):
    self.db_conn = DbConnection()

  # 添加
  def add(self, **kwargs):
    # 连接并获取到游标
    cursor = self.db_conn.connect()
    # sql语句 -> 插入
    sql = """ insert into permission(%s) values(%s) """
    key_list = []
    value_list = []
    for k, v in kwargs.items():
      key_list.append(k)
      # %% => 字符'%'
      value_list.append('%%(%s)s' % k)
    sql = sql % (','.join(key_list), ','.join(value_list))
    # 执行
    cursor.execute(sql, kwargs)
    # 提交执行并关闭
    self.db_conn.close()

  # 获取数据
  def fetch_all(self):
    # 1. 先连接
    cursor = self.db_conn.connect()
    '''
      caption -> 操作名称
      module -> 位于哪个模块内
      func -> 模块内的方法名
    '''
    sql = """ 
      select 
        nid,
        caption,
        module,
        func
      from
        permission
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    self.db_conn.close()
    return result

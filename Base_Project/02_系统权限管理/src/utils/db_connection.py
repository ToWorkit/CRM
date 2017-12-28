# -*- coding:utf-8 -*-
import pymysql
# 引入设置文件
from config import settings

# 数据库操作
class DbConnection:
  def __init__(self):
    self.__conn_dict = settings.PY_MYSQL_CONN_DICT
    self.conn = None
    self.cursor = None

  # 连接
  def connect(self, cursor = pymysql.cursors.DictCursor):
    # 创建连接
    self.conn = pymysql.connect(**self.__conn_dict)
    # 游标参数（设置值为字典）
    self.cursor = self.conn.cursor(cursor=cursor)

  # 提交和关闭操作
  def close(self):
    self.conn.commit()
    self.cursor.close()
    self.conn.close()

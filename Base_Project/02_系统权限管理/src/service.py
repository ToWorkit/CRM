# -*- coding:utf-8 -*-

from src.repository.user_info import UserInfoRepository
from src.repository.user_type_to_permission import UserTypeToPermissionRepository
from src.utils import commons
from config import settings

import importlib

# 选择
def choice_menu():
  print('登录成功: %s' % settings.current_user_info['username'])
  while  True:
    # 拿到所有权限 -> 序号形式
    for i, item in enumerate(settings.current_user_permission_list, 1):
      print(i, item['caption'])
    choice = input('请输入菜单: ')
    choice = int(choice)
    # 获取输入的对应权限
    permission = settings.current_user_permission_list[choice - 1]
    # 获取模块路径
    module = permission['module']
    # 获取方法名
    func_name = permission['func']
    # 动态导入模块，并通过反射执行指定的方法
    m = importlib.import_module(module)
    func = getattr(m, func_name)
    func()
# 
def find_pwd():
  pass

# 注册
def register():
  '''
  输入用户名
  输入密码
  输入邮箱
  判断用户名是否存在
  '''
  obj = UserInfoRepository()
  ret = obj.exist('root')
  if ret:
    print('已经存在')
  else:
    # 没有就去注册
    # obj.create()
    pass
  # 将数据插入到userinfo表中
  
def login():
  while True:
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    # md5加密
    pwd = commons.md5(password)
    # 用户信息
    user_repository = UserInfoRepository()
    # 当前登录的用户信息
    user_info = user_repository.fetch_by_user_pwd(username, pwd)
    if not user_info:
      print('用户名或密码错误，请重新输入')
      continue
    # 权限
    type_to_per_repository = UserTypeToPermissionRepository()
    # 获取登录用户名的权限信息
    permission_list = type_to_per_repository.fetch_permission_by_type_id(user_info['user_type_id'])

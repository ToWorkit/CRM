# -*- coding:utf-8 -*-

# md5加密
import hashlib

def md5(arg):
  m = hashlib.md5()
  m.update(bytes(arg, encoding='utf8'))
  return m.hexdigest()

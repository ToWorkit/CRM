from django.db import models

# Create your models here.

# 数据库
class UserInfo(models.Model):
  # 创建字段(长度)
  username = models.CharField(max_length = 64)
  sex = models.CharField(max_length = 64)
  email = models.CharField(max_length = 64)

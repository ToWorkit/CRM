from django.db import models

# Create your models here.

# 数据库
# 首先设计表结构

class Customer(models.Model):
  '''客户信息表'''
  '''
    32 字节(utf8格式中文一个占3个字节) 
    限制django
    可为空
    blank，null -> 一般成对出现
  '''
  name = models.CharField(max_length=32, blank=True, null=True)
  # unique -> 唯一
  qq = models.CharField(max_length=64, unique=True)
  qq_name = models.CharField(max_length=64, blank=True, null=True)
  phone = models.CharField(max_length=64, blank=True, null=True)
  # 选择来源
  source_choices = (
    (0, '转介绍'),
    (1, 'qq群'),
    (2, '官网'),
    (3, '百度推广')
    (4, '51CTO'),
    (5, '知乎'),
    (6, '市场')
  )
  # 选择
  # SmallIntegerField -> 省空间(只是选择数字而已)
  source = models.SmallIntegerField(choices=source_choices)
  # 转介绍信息
  referral_from = models.CharField(verbose_name='转介绍人qq', max_length=64, blank=True, null=True)
class CustomerFollowUp(models.Model):
  '''客户跟进表'''
  pass

class Course(models.Model):
  '''课程表'''
  pass

class ClassList(models.Model):
  '''班级表'''
  pass

class CourseRecord(models.Model):
  '''上课记录表'''
  pass

class StudyRecord(models.Model):
  '''学习记录表'''
  pass

class Enrollment(models.Model):
  '''报名表'''
  pass

class UserProfile(models.Model):
  '''账号表'''
  pass

class Role(models.Model):
  '''角色表'''
  pass



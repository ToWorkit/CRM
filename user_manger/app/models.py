from django.db import models

# Create your models here.

# 班级表
class Classes(models.Model):
  caption = models.CharField(max_length=32)
  # 指定关联，且test必须唯一(unique)
  # test = models.CharField(max_length=32, unique=True)
   
# 学生表
class Student(models.Model):
  name = models.CharField(max_length=32)
  email = models.CharField(max_length=32, null=True)
  # 绑定外键，建立一对多的关系，班级为 一 ，学生为 多
  # 默认关联主键
  cls = models.ForeignKey(
          'Classes', 
          on_delete=models.CASCADE,
        )
  # 指定关联
  '''cls = models.ForeignKey(
          'Classes', 
          on_delete=models.CASCADE,
          to_filed='test'
        )'''


# 教师表
class Teacher(models.Model):
  name = models.CharField(max_length=32)
  # 建立多对多的关系(老师和班级)
  cls = models.ManyToManyField('Classes')

# 创建管理员登录表
class Administrator(models.Model):
  username = models.CharField(max_length=32)
  password = models.CharField(max_length=32)


# 三级联动
# 省
class Province(models.Model):
  name = models.CharField(max_length=32)

# 市
class City(models.Model):
  name = models.CharField(max_length=32)
  # 一对多
  pro = models.ForeignKey('Province', on_delete=models.CASCADE)

# 县
class Xian(models.Model):
  name = models.CharField(max_length=32)
  cy = models.ForeignKey('City', on_delete=models.CASCADE)

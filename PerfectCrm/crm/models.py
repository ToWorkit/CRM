from django.db import models

# Create your models here.

class Customer(models.Model):
  '''客户信息表'''
  # 字节，设置Django的admin可以不填写(为了保存时可以通过检测，仅仅限制admin而非数据库属性)，可为空(首次接触不一定告诉姓名)
  name = models.CharField(max_length = 32, blank = True, null = True)
  # unique -> 唯一
  qq = models.CharField(max_length = 64, unique = True)
  qq_name = models.CharField(max_length = 64, blank = True, null = True)
  phone = models.CharField(max_length = 64, blank = True, null = True)
  # 来源选择
  source_choices = (
    (0, '转介绍'),
    (1, 'QQ群'),
    (2, '官网'),
    (3, '百度推广'),
    (4, '51CTO'),
    (5, '知乎'),
    (6, '市场推广')
    )
  # 选择整数字段
  source = models.SmallIntegerField(choices = source_choices)
  # 转介绍的备注信息
  referral_from = models.CharField(verbose_name = '转介绍人qq', max_length = 64, blank = True, null = True)

  # 外键，与课程表建立连接
  consult_course = models.ForeignKey('Course'. verbose_name = '咨询课程')
  # 文本内容，咨询的详情
  content = models.TextField(verbose_name = '咨询详情')

  # 标签(可以给一个客户身上打多个标签，一个标签也可以对应多个客户) -> 多对多的关系
  tags = models.ManyToManyField('Tag', blank = True, null = True)
  
  # 与账号表建立连接(分配账号)
  consultant = models.ForeignKey('UserProfile')
  # 备忘录
  memo = models.TextField(blank = True, null = True)
  # 时间(自动添加当前时间)
  date = models.DateTimeField(auto_now_add = True)

  # 关联数据，其他表关联当前表时可以获取qq(因为qq是唯一的，可以通过qq进行查询当前表获取更多的数据)
  def __str__(self):
    return self.qq


class Tag():
  '''客户标签'''
  name = models.CharField(unique = True, max_length = 32)
  # 对外关联表开放数据
  def __str__(self):
    return self.name


class CustomerFollowUp(models.Model):
  '''客户跟进表'''
  # 管理客户信息表
  customer = models.ForeignKey('Customer')
  content = models.TextField(verbose_name = '根据内容')
  # 账号信息
  consultant = models.ForeignKey('UserProfile')
  date = models.DateTimeField(auto_now_add = True)
  # 客户意向选择
  intention_choices = (
    (0, '2周内报名'),
    (1, '1个月内报名'),
    (2, '近期无报名计划'),
    (3, '已在其他机构报名'),
    (4, '已报名'),
    (5, '已拉黑'),
    )
  # 根据选择内容选择对应的标号
  intention = models.SmallIntegerField(choices = intention_choices)
  date = models.DateTimeField(auto_now_add = True)
  # 对外关联表开放数据
  def __str__(self):
    return "<%s : %s>" %(self.customer.qq, self.intention)


class UserProfile(models.Model):
  '''账号表'''
  pass

class Course(models.Model):
  '''课程表'''
  # 唯一
  name = models.CharField(max_length = 64, unique = True)
  # 价格
  price = models.PositiveSmallIntegerField()
  # 周期
  period = models.PositiveSmallIntegerField(verbose_name = '周期(月)')
  # 课程大纲
  outline = models.TextField()

  def __str__(self):
    return self.name

class Branch(models.Model):
  '''校区'''
  name = models.CharField(max_length = 128, unique = True)
  # 地址
  addr = models.CharField(max_length = 128)
  def __str__(self):
    return self.name 

class ClassList(models.Model):
  '''班级表'''
  # 校区， 多对多的关系
  branch = models.ManyToManyField('')
  # 关联课程表
  course = models.ForeignKey('Course')
  # 学期
  semester = models.PositiveSmallIntegerField(verbose_name = '学期')
  # 老师(一个老师对应多个学生，一个学生也可以对应多个老师) -> 多对多的关系
  teachers = models.ManyToManyField('UserProfile')

class CourseRecord(models.Model):
  '''上课记录'''
  pass

class StudyRecord(models.Model):
  '''学习记录'''
  pass

class Enrollment(models.Model):
  '''报名表'''
  pass

class Role(models.Model):
  '''角色表'''
  pass

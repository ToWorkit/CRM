from django.db import models
# django 自带的验证模块 
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
  '''客户信息表'''
  # 字节，blank -> 设置Django的admin可以不填写(为了保存时可以通过检测，仅仅限制admin而非数据库属性)，可为空(首次接触不一定告诉姓名)
  # https://www.jianshu.com/p/c10be59aad7a
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
  consult_course = models.ForeignKey('Course', verbose_name = '咨询课程', on_delete = models.CASCADE)
  # 文本内容，咨询的详情
  content = models.TextField(verbose_name = '咨询详情')

  # 标签(可以给一个客户身上打多个标签，一个标签也可以对应多个客户) -> 多对多的关系
  tags = models.ManyToManyField('Tag', blank = True, null = True)
  
  # 与账号表建立连接(分配账号)
  consultant = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
  # 备忘录
  memo = models.TextField(blank = True, null = True)
  # 时间(自动添加当前时间)
  date = models.DateTimeField(auto_now_add = True)
  # 实力静态化，推荐写法，以防止页面上直接显示时出现 object 
  # https://code.ziqiangxuetang.com/django/django-admin.html
  def __str__(self):
    return self.qq


class Tag():
  '''客户标签'''
  name = models.CharField(max_length = 32, unique = True)
  # 对外关联表开放数据
  def __str__(self):
    return self.name


class CustomerFollowUp(models.Model):
  '''客户跟进表'''
  # 管理客户信息表
  customer = models.ForeignKey('Customer', on_delete = models.CASCADE)
  content = models.TextField(verbose_name = '根据内容')
  # 账号信息
  consultant = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
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
  # 校区
  branch = models.ForeignKey('Branch', verbose_name = '校区', on_delete = models.CASCADE)
  # 课程表
  course = models.ForeignKey('Course', on_delete = models.CASCADE)
  # 班级类型
  class_type_choices = (
    (0, '面授(脱产)'),
    (1, '面授(周末)'),
    (2, '网络班')
    )
  class_type = models.SmallIntegerField(choices = class_type_choices, verbose_name = '班级类型')
  # 学期
  semester = models.PositiveSmallIntegerField(verbose_name = '学期')
  # 老师(一个老师对应多个学生，一个学生也可以对应多个老师) -> 多对多的关系
  teachers = models.ManyToManyField('UserProfile')
  # 开班时间
  start_date = models.DateField(verbose_name = '开班日期')
  end_date = models.DateField(verbose_name = '结业日期', blank = True, null = True)
  def __str__(self):
    return "%s %s %s" % (self.branch, self.course, self.semester)
  # 联合唯一 -> 同一个校区的同一门课程只能有一个 1 期，下一期就为 2 期，不允许再为 1 期
  class Meta:
    unique_together = ('branch', 'course', 'semester')


class CourseRecord(models.Model):
  '''上课记录'''
  # 哪个班级
  from_class = models.ForeignKey('ClassList', verbose_name = '班级', on_delete = models.CASCADE)
  # 第几次
  day_num = models.PositiveSmallIntegerField(verbose_name = '第几节(天)')
  # 老师
  teacher = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
  # 有没有作业
  has_homework = models.BooleanField(default = True)
  # 作业标题
  homework_title = models.CharField(max_length = 128, blank = True, null = True)
  # 作业内容
  homework_content = models.TextField(blank = True, null = True)
  # 课程大纲
  outline = models.TextField(verbose_name = '本节课程大纲')
  # 上课时间
  date = models.DateField(auto_now_add = True)
  # 实例静态化(print 时自动调用，方便调试)
  def __str__(self):
    return '%s %s' % (self.from_class, self.day_num)
  # 联合唯一
  class Meta:
    unique_together = ('from_class', 'day_num')


class StudyRecord(models.Model):
  '''学习记录'''
  # 学生
  student = models.ForeignKey('Enrollment', on_delete = models.CASCADE)
  # 上课记录
  course_record = models.ForeignKey('CourseRecord', on_delete = models.CASCADE)
  # 出勤记录
  attendance_choices = (
    (0, '已签到'),
    (1, '迟到'),
    (2, '缺勤'),
    (3, '早退')
    )
  attendance = models.SmallIntegerField(choices = attendance_choices, default = 0, verbose_name = '出勤记录')
  # 分数
  score_choices = (
    (100, 'A+'),
    (90, 'A'),
    (85, 'B+'),
    (80, 'B'),
    (75, 'B-'),
    (70, 'C+'),
    (60, 'C'),
    (40, 'C-'),
    (-50, 'D'),
    (-100, 'COPY'),
    (0, 'N/A')
    )
  score = models.SmallIntegerField(choices = score_choices, default = 0, verbose_name = '分数')
  # 备注
  memo = models.TextField(blank = True, null = True)
  date = models.DateField(auto_now_add = True)
  def __str__(self):
    return "%s %s %s" %(self.student, self.course_record, self.score)


class Enrollment(models.Model):
  '''报名表'''
  # 关联客户表
  customer = models.ForeignKey('Customer', on_delete = models.CASCADE)
  # 关联班级表
  enrolled_class = models.ForeignKey('ClassList', verbose_name = '所报班级', on_delete = models.CASCADE)
  # 关联账号表
  # 接待该客户的销售人员
  consultant = models.ForeignKey('UserProfile', verbose_name = '课程顾问', on_delete = models.CASCADE)
  # 合同, 默认为False, 同意后为True
  contract_agreed = models.BooleanField(default = False, verbose_name = '学员已同意合同条款')
  contract_approved = models.BooleanField(default = False, verbose_name = '学校已同意合同条款')
  # 精确到 时分
  date = models.DateTimeField(auto_now_add = True)
  def __str__(self):
    return '%s %s' % (self.customer, self.enrolled_class)
  # 联合唯一
  class Meta:
    # 一个学员只能报一期
    unique_together = ('customer', 'enrolled_class')


class Payment(models.Model):
  '''缴费记录'''
  # 关联客户表
  customer = models.ForeignKey('Customer', on_delete = models.CASCADE)
  # 关联课程
  course = models.ForeignKey('Course', verbose_name = '所报课程', on_delete = models.CASCADE)
  # 大数字，不能使用Small
  amount = models.PositiveIntegerField(verbose_name = '数额', default = 500)
  # 接待顾问(办理的人)
  consultant = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
  date = models.DateTimeField(auto_now_add = True)
  def __str__(self):
    return '%s %s' % (self.customer, self.amount)

class UserProfile(models.Model):
  '''账号表'''
  # 关联django自带的用户表, OneToOneField -> 单对单，各自有且仅有对方可以关联
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  name = models.CharField(max_length = 32, unique = True)
  # 角色表, 多对多
  roles = models.ManyToManyField('Role', blank = True, null = True)
  def __str__(self):
    return self.name


class Role(models.Model):
  '''角色表'''
  name = models.CharField(max_length = 32, unique = True)
  def __str__(self):
    return self.name

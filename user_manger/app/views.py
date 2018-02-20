from django.shortcuts import render, HttpResponse, redirect

# 装饰器
from django.utils.decorators import method_decorator

from app import models

import json

# Create your views here.
'''
def login(req):
  # 向管理员表中写入数据
  # models.Administrator.objects.create(
  #   username = 'c',
  #   password = '123'
  # )
  message = ''
  if req.method == 'POST':
    # 获取提交的数据
    user = req.POST.get('user')
    pwd = req.POST.get('pwd')

    # 在管理员表中查找用户名和密码 -> 个数
    c = models.Administrator.objects.filter(username=user, password=pwd).count()

    if c:
      # 将用户名添加至cookies
      rep = redirect('/index') # 重定向并携带cookie
      # 指定超时时间 max_age
      rep.set_cookie('username', user, max_age=10)
      rep.set_cookie('email', user + '@email.com')
      return rep

    else:
      message = '用户名或者密码错误'
  return render(req, 'login.html', {'msg': message})

def index(req):
  # 用户必须登录，否则返回登录页
  username = req.COOKIES.get('username')
  if username:
    return render(req, 'index.html', {'username': username})
  else:
    return redirect('/login')

def test(req):
  obj = HttpResponse('ok')
  # obj.set_cookie('name', 'ml') 
  # path='/test' -> 设置cookie读取url限制，只有访问 /test 时才可以获取
  # domain='test.com' -> 设置顶级域名，www.test.com，dem.test.com(二级域名)下都可以获取cookie
  # obj.set_cookie('name_1', 'lm', domain='test.com' ) 
  
  # 不设置默认是当前域名，只在当前域名下可以访问到cookie 
  # obj.set_cookie('name_1', 'lm')
  
  # 加密设置cookie
  obj.set_signed_cookie('username', 'emmm')

  return obj

def getCookie(req):
  # ck = req.COOKIES.get('username ')
  
  # 获取加密的cookie
  ck = req.get_signed_cookie('username')
  return HttpResponse(ck)

'''
# CBV -> 类形式
from django import views


class Login(views.View):

  def get(self, request, *args, **kwargs):
    return render(request, 'login.html', {'msg': ''})

  def post(self, request, *args, **kwargs):
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 在管理员表中查找用户名和密码 -> 个数
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
            return render(request,'login.html', {'msg': message})


# FBV -> 函数方式
# session
'''
def login(request):
    message = ""
    # v = request.session
    # print(type(v))
    from django.contrib.sessions.backends.db import SessionStore
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 在管理员表中查找用户名和密码 -> 个数
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
    obj = render(request,'login.html', {'msg': message})
    # return obj
'''

def logout(request):
    request.session.clear()
    return redirect('/login.html')



def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login.html')
    return inner

@auth
def index(request):
    current_user = request.session.get('username')
    return render(request, 'index.html',{'username': current_user})
 
@auth
def handle_classes(request):
  # 请求数据
  if request.method == 'GET':

    # for i in range(100):
    #   models.Classes.objects.create(caption="三年二班" + str(i))

    current_user = request.session.get('username')
    # 添加一部分测试数据
    # models.Classes.objects.create(caption="三年七班")
    # models.Classes.objects.create(caption="三年二班")
    # models.Classes.objects.create(caption="三年四班")
    # 获取所有的班级列表
    # cls_list = models.Classes.objects.all()
    
    # 当前页
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    # 所有数据的个数
    total_count = models.Classes.objects.all().count()

    # 引入分页函数
    from utils.page import PagerHelper
    # 总数，页码，当前分页url，页数
    obj = PagerHelper(total_count, current_page, '/classes.html', 10)
    pager = obj.pager_str()

    cls_list = models.Classes.objects.all()[obj.db_start:obj.db_end]
    # from django.utils.safestring import mark_safe -> 渲染django
    return render(request, 'classes.html', {'username': current_user,'cls_list': cls_list, 'str_pager': pager})
  # 添加数据
  elif request.method == 'POST':
    # Form表单的提交方式
    '''
      caption = request.POST.get('caption', None) # 默认为None
      models.Classes.objects.create(caption=caption)
      return redirect('/classes.html')
    '''
    # ajax的请求处理
    response_dict = {'status': True, 'error': None, 'data': None}
    caption = request.POST.get('caption', None)
    if caption:
      # 新增数据
      obj = models.Classes.objects.create(caption=caption)
      response_dict['data'] = {'id': obj.id, 'caption': obj.caption}
    else:
      response_dict['status'] = False
      response_dict['error'] = '标题不能为空'
    # json格式 -> ajax返回数据前端作处理
    return HttpResponse(json.dumps(response_dict))

@auth
def handle_add_classes(request):
  message = ''
  if request.method == 'GET':
    return render(request, 'add_classes.html', {'msg': message})
  elif request.method == 'POST':
    caption = request.POST.get('caption', None)
    if caption:
      models.Classes.objects.create(caption=caption)
    else:
      message = '标题不能为空'
      return render(request, 'add_classes.html', {'msg': message})
    return redirect('classes.html')
  else:
    return redirect('/index.html')

@auth
def handle_edit_classes(request):
  if request.method == 'GET':
    nid = request.GET.get('nid')
    obj = models.Classes.objects.filter(id=nid).first()
    return render(request, 'edit_classes.html', {'obj': obj})
  elif request.method == 'POST':
    nid = request.POST.get('nid')
    caption = request.POST.get('caption')
    models.Classes.objects.filter(id=nid).update(caption=caption)
    return redirect('/classes.html')
  else:
    return redirect('/index.html')

@auth # 使用装饰器验证是否登录
def add_student(request):
  if request.method == 'GET':
    # 取班级表前20条数据
    cls_list = models.Classes.objects.all()[0:20]
    return render(request, 'add_student.html', {'cls_list': cls_list})
  elif request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    cls_id = request.POST.get('cls_id')
    models.Student.objects.create(name=name, email=email, cls_id=cls_id)
    return redirect('/student.html')

@auth
def handle_student(request):
    if request.method == 'GET':
      # for i in range(10):
      #   # print(i)
      #   models.Student.objects.create(
      #     name = "root" + str(i),
      #     email = 'root' + str(i) + '@qq.com',
      #     cls_id = str(int(i) + 1)
      #     )
      result = models.Student.objects.all()
      current_user = request.session.get('username')
      return render(request, 'student.html', {'username': current_user,'result': result})
    elif request.method == "POST":
        return redirect('/index.html')
    else:
        return redirect('/index.html')

@auth
def edit_student(request):
  if request.method == 'GET':
    # 班級列表前20
    cls_list = models.Classes.objects.all()[:20]
    nid = request.GET.get('nid')
    # 根据id查找
    # obj = models.Student.objects.filter(id=nid)[0]
    obj = models.Student.objects.get(id=nid)
    # print(obj)
    return render(request, 'edit_student.html', {'cls_list': cls_list, 'obj': obj})
  elif request.method == 'POST':
    nid = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    cls_id = request.POST.get('cls_id')
    models.Student.objects.filter(id=nid).update(name=name, email=email, cls_id=cls_id)
    return redirect('/student.html')

@auth
def handle_teacher(request):
    current_user = request.session.get('username')
    return render(request, 'teacher.html', {'username': current_user})

# menu
def menu(request):
  # for i in range(10):
  #   models.City.objects.create(name="西安_" + str(i), pro_id=1)
  # return HttpResponse('OK')
  pro_list = models.Province.objects.all()
  return render(request, 'menus.html', {'pro_list': pro_list})

# 城市
def fetch_city(request):
  # 根据省份id获取相关的城市
  # rep = {'status': 200, 'error': None, 'data': None}
  
  province_id = request.GET.get('province_id')
  # 查找
  result = models.City.objects.filter(pro_id=province_id).values('id', 'name')
  # QuerySet -> 内部放置对象
  # https://www.cnblogs.com/linxiyue/p/4040262.html
  result = list(result)
  # 发给页面json格式数据
  data = json.dumps(result)
  return HttpResponse(data)

# 县
def fetch_xian(request):
  city_id = request.GET.get('city_id')
  result = models.Xian.objects.filter(cy_id=city_id).values('id', 'name')
  result = list(result)
  return HttpResponse(json.dumps(result))

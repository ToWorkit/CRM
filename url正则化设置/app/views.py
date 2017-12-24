from django.shortcuts import render, HttpResponse, render_to_response, redirect

# models 数据文件
from app import models

import datetime
# Create your views here.
def cur_time(request):
  times = datetime.datetime.now()
  # return HttpResponse('<h1>Hello World</h1>')
  return render(request, 'cur_time.html', {'now_time': times})  

'''
user_list = []
# 视图函数
def userInfo(req):
  # 直接读取文件需要在 settings.py 的 templates 建立连接
  # " 'DIRS': [os.path.join(BASE_DIR, 'templates')], "
  
  # 判读请求方法
  if req.method == 'POST':
    # 有则取出 userName 的数据，没有返回None
    username = req.POST.get("username", None)
    sex = req.POST.get("sex", None)
    email = req.POST.get("email", None)
    user = {
      'username': username,
      'sex': sex,
      'email': email
    }
    # 储存多条信息
    user_list.append(user)
    return render(req, 'index.html', {'user_list': user_list})
  # req -> 所有请求信息
  return render(req, 'index.html')
'''

# 数据库操作
user_list = []
def userInfo(req):
  # 直接读取文件需要在 settings.py 的 templates 建立连接
  # " 'DIRS': [os.path.join(BASE_DIR, 'templates')], "
  
  # 判读请求方法
  if req.method == 'POST':
    # 有则取出 userName 的数据，没有返回None
    _username = req.POST.get("username", None)
    _sex = req.POST.get("sex", None)
    _email = req.POST.get("email", None)

    # 添加到数据库
    models.UserInfo.objects.create(
      username = _username,
      sex = _sex,
      email = _email,
    )

    # 取数据
    user_list = models.UserInfo.objects.all()
    return render(req, 'index.html', {'user_list': user_list})
  # req -> 所有请求信息
  return render(req, 'index.html')

def str_123(req):
  return HttpResponse('<h1 style="color: red">Hello World</h1>')

# 配合 urls 取值, 两个括号，对应两个参数
def _str(req, num, two):
  return HttpResponse('<h1 style="color: blue">Hello World -->'+ str(int(num) + int(two)) +'</h1>') 

# 有正则名称分组则需要通过相同的名称来匹配
def str_re(req, one, two):
  return HttpResponse('<h1 style="color: red">Hello' + one + two +'</h1>')

# 参数 -> 参数名需要保持一致
def index(req, name):
  return HttpResponse(name)

# 另一个参数
def index_2(req):
  print(req.GET)
  print(req.path)
  gender = '26'
  if req.method == 'POST':
    username = req.POST.get('username')
    pwd = req.POST.get('pwd')
    # 和数据库交互判断
    if username == 'a' and pwd == 'b':
      name = 'ml'
      age = '24'
      sex = 'nv'
      # return render(req, 'new.html', {'name': name})
      
      # locals -> 将变量全部传入, 都会取到，看new.html
      return render(req, 'new.html', locals())
      
      # 重定向
    else:
      return redirect('/app/index_2')

      # 需要引入
      # return render_to_response('new.html')
  return render(req, 'login.html')  


# 自己的路由自己处理
def introduce(req):
  return HttpResponse('ok')


def home(req):
  name = 'ml'
  return render(req, 'home.html', {'name': name})

# 
def login(req):
  if req.method == 'POST':
    username = req.POST.get('username')
    pwd = req.POST.get('pwd')
    if username == 'a' and pwd == 'b':
      return redirect('/home/')  # => 走home路由，会通过 home() 函数处理并返回
      # return render(req, 'home.html') # => 会直接返回home.html，不会经由home函数
  return render(req, 'login.html')

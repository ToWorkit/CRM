from django.shortcuts import render, HttpResponse, render_to_response

import datetime

# Create your views here.

def index(req):

  class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age

  s = 'Hello'
  s_2 = [1, 2, 3] # list
  s_3 = {'username': 'ml', 'sex': 'nv'} #dict
  s_4 = datetime.datetime.now()
  s_5 = Person('lm', 26)
  # return render(req, 'index.html', {'list': s_2})
  # return render(req, 'index.html', {'obj': s_3})
  # return render(req, 'index.html', {'obj': s_4})
  # return render(req, 'index.html', {'obj': s_5})
  # return render(req, 'index.html', {'obj': 'Hello'})
  
  return render(req, 'index.html', {'obj': '<a href="#">哈哈</a>'})

def login(req):
  if req.method == 'POST':
    return HttpResponse('ok')

  # return render(req, 'login.html')
  name = 'Hello World'
  num = 20
  return render(req, 'login.html', locals()) # 传入所有变量

def ordered(req):
  return render(req, 'ordered.html')

def shopping_car(req):
  return render(req, 'shopping_car.html')

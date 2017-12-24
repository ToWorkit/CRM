# 单个应用中的url
# 最后统一用全局的 urls 处理
from django.contrib import admin
from django.urls import path, include
# 使用 url 正则化路由得先引入
from django.conf.urls import url

from app import views

urlpatterns = [
    path('new/story', views.introduce),
    # # url 别名 => 后端修改后前端不需要再更改
    # # <form action={% url 'lm' %} method='post'>
    path('index_2/', views.index_2, name = "lm"),

]

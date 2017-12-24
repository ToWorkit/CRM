"""one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 使用 url 正则化路由得先引入
from django.conf.urls import url

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 每个应用的路由单独处理
    path('app/', include('app.urls')),

    path('login/', views.login),
    
    path('home/', views.home),
    # path('cur_time/', views.cur_time),
    # # 路径，视图函数
    # path('userInfo/', views.userInfo),
    # # 使用 url 正则化路由得先引入
    # url(r'^str/123/$', views.str_123),
    # # 获取到输入的数字 -> ()
    # url(r'^str/([0-9]{2})/([\d]{1})$', views._str),
    # # ?P => 固定格式，表示组，组名为<组名>，<>后面为正则匹配
    # url(r'^str_re/(?P<one>[0-9]{2})/(?P<two>[\d]{1})$', views.str_re),

    # # 参数值
    # path('index/', views.index, {'name': 'ml'}),

    # # url 别名 => 后端修改后前端不需要再更改
    # # <form action={% url 'lm' %} method='post'>
    # path('index_2/', views.index_2, name = "lm")
]

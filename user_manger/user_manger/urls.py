"""user_manger URL Configuration

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
from django.urls import path
# 使用 url 正则化路由得先引入
from django.conf.urls import url

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.login),
    
    # 类的写法
    path('login.html/', views.Login.as_view()),

    url(r'^logout.html$', views.logout),
    url(r'^index.html$', views.index),
    url(r'^classes.html$', views.handle_classes),
    url(r'^add_classes.html$', views.handle_add_classes),
    url(r'^edit_classes.html$', views.handle_edit_classes),
    url(r'^student.html$', views.handle_student),
    url(r'^teacher.html$', views.handle_teacher),
]

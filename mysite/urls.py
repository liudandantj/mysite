"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include       #include函数,url分解器，引入在别的app上写的urls.py
from polls import views
from project_app import urls

#polls登录密码，显示
#project_app项目和模块
#interface_app 用例和任务
#tools_app测试工具
urlpatterns=[path('admin/',admin.site.urls),
             path('',views.index),
             path('accounts/login/',views.index),
             path('login_action/',views.login_action),
             path('logout/',views.logout),
             path('manage/',include('project_app.urls'))]
             # path('project_manage/', views.project_manage),
             # path('add_project/',views.add_project)


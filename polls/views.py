from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth  #认证模块
from django.contrib.auth.decorators import login_required
from polls.models import Project,Module
#主要代码逻辑，非常重要
def index(request):
    # return HttpResponse('hello' )
    return render(request,'index.html')#返回请求和页面，传递context到template

# Create your views here.
#处理登录请求,查询数据库等
def login_action(request):
    if request.method == 'POST':#注意大写
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == '' or password == '':
            return render(request, 'index.html',
                          {'error':'用户名或密码不能为空'}
                          )
        else:
            user=auth.authenticate(username=username,password=password)
            print(user)

            if user is not None:
               auth.login(request,user)   #记录用户登录状态
               response= HttpResponseRedirect('/project_manage/')#跳转到某一指定的页面，没有参数
               #response.set_cookie('user',username,3600)#
               request.session['user']=username
               return response
               #return render(request, 'project_manage.html',{'user':user})
            else:
                return render(request, 'index.html',{'error':'用户名或密码错误'})
@login_required #判断用户是否登录

def logout(request):
    auth.logout(request)#清除用户登录状态
    response= HttpResponseRedirect('/')#跳转到主界面
    return response




        # if username =='admin' and password=='123456':
        #     return render(request, 'project_manage.html'
        #                    )
        # else:
        #     return render(request,'index.html',{'error':'用户名或密码错误'})
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth  #认证模块
#主要代码逻辑，非常重要
def index(request):
    # return HttpResponse('hello' )
    return render(request,'index.html')

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
            print(type(user))
            if user is not None:
               auth.login(request,user)   #验证登陆
               return render(request, 'project_manage.html')
            else:
                return render(request, 'index.html',{'error':'用户名或密码错误'})



        # if username =='admin' and password=='123456':
        #     return render(request, 'project_manage.html'
        #                    )
        # else:
        #     return render(request,'index.html',{'error':'用户名或密码错误'})
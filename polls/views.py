from django.http import HttpResponse
from django.shortcuts import render
#主要代码逻辑，非常重要
def index(request):
    # return HttpResponse('hello' )
    return render(request,'index.html')

# Create your views here.
#处理登录请求,查询数据库等
def login_action(request):
    if request.model == 'GET':#注意大写
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username == '' or password == '':
            return render(request, 'index.html',
                          {'error':'用户名或密码不能为空'}
                          )

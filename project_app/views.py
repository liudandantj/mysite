from django.shortcuts import render
from project_app.models import Project
from django.contrib.auth.decorators import login_required
def project_manage(request):
    #username=request.COOKIES.get('user','')
    username=request.session.get('user','')#读取浏览器session
    project_all=Project.objects.all()
    print(project_all)
    return render(request,'project_manage.html',{
        'user':username,
        'projects':project_all,
        'type':'list'
    })
def add_project(request):
    #添加项目
    return render(request,'project_manage.html',{'type':'add'})


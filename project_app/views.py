from django.shortcuts import render
def project_manage(request):
    #username=request.COOKIES.get('user','')
    username=request.session.get('user','')#读取浏览器session
    project_all=Project.objects.all()
    print(project_all)
    return render(request,'project_manage.html',{'user':username,'projects':project_all})



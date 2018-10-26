from django.shortcuts import render
from project_app.models import Project
from django.contrib.auth.decorators import login_required
from project_app.forms import ProjectForm
from django.http import HttpResponseRedirect
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            print(name)
            print(describe)
            Project.objects.create(name=name,describe=describe)
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/project_manage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()

    return render(request, 'project_manage.html', {'type':'add',
                                                   'form': form})
def edit_project(request,pid):
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            model=Project.objects.get(id=pid)

            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.status = form.cleaned_data['status']
            model.save
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        if pid:
            form = ProjectForm(instance=Project.objects.get(id=pid))
        else:
            form = ProjectForm()

    return render(request, 'project_manage.html', {'type':'edit',
                                                   'form': form})
def delete_project(request,pid):
    if request.method == 'POST':
       pass
    else:
        form = ProjectForm()

    return render(request, 'project_manage.html', {'type':'delete',
                                                   'form': form})





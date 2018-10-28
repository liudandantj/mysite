from django.shortcuts import render
from project_app.models import Module
from django.contrib.auth.decorators import login_required
from project_app.forms import ModuleForm
from django.http import HttpResponseRedirect
def module_manage(request):
    #username=request.COOKIES.get('user','')
    username=request.session.get('user','')#读取浏览器session
    module_all=Module.objects.all()
    print(module_all)
    return render(request,'module_manage.html',{
        'user':username,
        'modules':module_all,
        'type':'list'
    })

def add_module(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModuleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project=form.cleaned_data['project']
            Module.objects.create(name=name,describe=describe,project=project)
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/module_manage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModuleForm()

    return render(request, 'module_manage.html', {'type':'add',
                                                   'form': form})
def edit_module(request,mid):
    if request.method == 'POST':
        form=ModuleForm(request.POST)
        if form.is_valid():
            model=Module.objects.get(id=mid)

            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.project = form.cleaned_data['project']
            model.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        if mid:
            form = ModuleForm(instance=Module.objects.get(id=mid))
        else:
            form = ModuleForm()

    return render(request, 'module_manage.html', {'type':'edit',
                                                   'form': form})
def delete_module(request,mid):
    Module.objects.get(id=mid).delete()
    return HttpResponseRedirect('/manage/module_manage/')
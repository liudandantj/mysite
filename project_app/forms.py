from django import forms
from project_app import models
from project_app.models import Project,Module
#from django.forms import ModelForm

'''class ProjectForm(forms.Form):
    name=forms.CharField(label='名称',max_length=100)
    describe=forms.CharField(label='描述',widget=forms.Textarea)
    status = forms.BooleanField(label='状态')'''


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
        # exclude=['create_time']
    #
    # form = ProjectForm()
    # form = ProjectForm(instance=project)
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'describe', 'project']

from django.contrib import admin
from project_app.models import Project,Module

# Register your models here.
#django自带一个admin后台，例如添加管理，管理员权限
class ProjectAdmin(admin.ModelAdmin):
    list_display=['name','describe','status','create_time','id']
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','project','describe','create_time','id']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Module,ModuleAdmin)


from django.db import models
# ORM 创建数据库表


class Project(models.Model):#项目表
    name = models.CharField('名称',max_length=50,blank=False,null=True)
    describe = models.TextField('描述',default='')
    status = models.BooleanField('状态',default=True)
    create_time = models.DateTimeField('创建时间',auto_now=True)
    def __str__(self):
        return self.name
class Module(models.Model):#模块表
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name =models.CharField('名称',max_length=100,blank=False,null=True)
    describe = models.TextField('描述', default='')
    create_time = models.DateTimeField('创建时间', auto_now=True)





from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from project_app.models import Project
from project_app.views.project_views import add_project

class ProjectTestCase(TestCase):
    """项目管理测试"""
    def setUp(self):
        """创建用户"""
        User.objects.create_user("test01", "test01@email.com","test123456")
        """创建项目"""
        Project.objects.create(name='project_abc',describe='project_abc的详情')
        self.client = Client()
        """用户登录"""
        login_data = {'username': 'test02', 'password': 'test12345678'}
        self.client.post('/login_action/', data=login_data)

    def test_project_select(self):
        """验证项目查询功能"""
        project = Project.objects.get(name="project_abc")
        self.assertEqual(project.describe, "project_abc的详情")
    def test_project_create(self):
        """验证项目创建功能"""
        Project.objects.create(name='project_abcd', describe='project_abcd的详情')
        project = Project.objects.get(name="project_abcd")
        self.assertEqual(project.describe, "project_abcd的详情")
    def test_project_update(self):
        """验证项目更新功能"""
        project = Project.objects.get(name="project_abc")
        project.name='project_abcde'
        project.describe='project_abcde的详情'
        project.save()
        project2=Project.objects.get(name='project_abcde')
        self.assertEqual(project2.describe, "project_abcde的详情")

    def test_project_delete(self):
        """验证项目删除功能"""
        project = Project.objects.get(name="project_abc")
        project.delete()
        projects=Project.objects.all()
        self.assertEqual(len(projects),0)

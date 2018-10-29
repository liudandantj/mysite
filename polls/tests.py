# Create your tests here.
#django单元测试
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class UserTestCase(TestCase):
    def setUp(self):
        """创建用户"""
        User.objects.create_user("test01", "test01@email.com","test123456")

    def test_user_select(self):
        """验证查询功能"""
        user = User.objects.get(username="test01")
        self.assertEqual(user.email, "test01@email.com")
    def test_user_create(self):
        """验证创建功能"""
        User.objects.create_user("test02", "test02@email.com", "test12345678")
        user = User.objects.get(username="test02")
        self.assertEqual(user.email, "test02@email.com")

    def test_user_update(self):
        """验证更新用户功能"""
        user = User.objects.get(username="test01")
        user.username='test03'
        user.email='test03@email.com'
        user.save()
        user2 = User.objects.get(username="test03")
        self.assertEqual(user2.email, "test03@email.com")

    def test_user_delete(self):
        """验证删除用户功能"""
        user = User.objects.get(username="test01")
        user.delete()
        users = User.objects.all()
        self.assertEqual(len(users), 0)

class IndexTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index(self):
        """测试登录页面返回"""
        # Issue a GET request.
        response = self.client.get('/')
        print(response.content.decode('utf-8'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

class LoginActionTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        User.objects.create_user("test02", "test02@email.com", "test12345678")
        self.client = Client()

    def test_login_null(self):
        """测试用户名和密码为空"""
        # Issue a GET request.
        login_data ={'username': '', 'password': ''}
        response = self.client.post('/login_action/',data=login_data)

        login_html=response.content.decode('utf-8')

        # Check that the response is 200 OK.
        self.assertIn('用户名或密码不能为空',login_html)

    def test_login_error(self):
        """测试用户名密码错误"""
        login_data = {'username': 'test01', 'password': 'test01'}
        response = self.client.post('/login_action/', data=login_data)

        login_html = response.content.decode('utf-8')

        # Check that the response is 200 OK.
        self.assertIn('用户名或密码错误', login_html)
    def test_login_success(self):
        """测试登录成功"""
        """测试用户名密码错误"""
        login_data = {'username': 'test02', 'password': 'test12345678'}
        response = self.client.post('/login_action/', data=login_data)

        login_html = response.content.decode('utf-8')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 302)



from django.test import TestCase
from django.test import TestCase
from django.conf import settings
import os


# Create your tests here.

class UserCenterTest(TestCase):
    def test_login_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'UserCenter/login.html')
        self.assertTrue(os.path.exists(template_base_path))

    def test_register_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'UserCenter/register.html')
        self.assertTrue(os.path.exists(template_base_path))

    def test_profile_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'UserCenter/profile.html')
        self.assertTrue(os.path.exists(template_base_path))

    def test_login(self):
        response = self.client.get('/UserCenter/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UserCenter/login.html')

    def test_register(self):
        response = self.client.get('/UserCenter/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UserCenter/register.html')

    def test_profile(self):
        response = self.client.get('/UserCenter/profile/')
        self.assertEqual(response.status_code, 302)

    def test_sign_out(self):
        response = self.client.get('/UserCenter/sign_out/')
        self.assertEqual(response.status_code, 302)

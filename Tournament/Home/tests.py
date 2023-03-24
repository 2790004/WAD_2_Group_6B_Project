from django.test import TestCase
from django.test import TestCase
from django.conf import settings
import os


# Create your tests here.

class HomeTest(TestCase):
    def test_base_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'base.html')
        self.assertTrue(os.path.exists(template_base_path))

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_index_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'base.html')
        self.assertTrue(os.path.exists(template_base_path))
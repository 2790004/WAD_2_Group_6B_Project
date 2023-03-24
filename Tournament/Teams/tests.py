from django.test import TestCase
from django.test import TestCase
from django.conf import settings
import os


# Create your tests here.

class TeamsTest(TestCase):
    def test_list_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'Team/list.html')
        self.assertTrue(os.path.exists(template_base_path))

    def test_list(self):
        response = self.client.get('/teams/list/')
        self.assertEqual(response.status_code, 302)

    def test_from_tournament_get_team_list_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'Team/from_tournament_get_team_list.html')
        self.assertTrue(os.path.exists(template_base_path))






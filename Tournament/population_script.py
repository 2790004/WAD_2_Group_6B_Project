import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()

from FilesManage.models import Pictures
from Teams.models import Teams, Team2User
from Tournaments.models import Tournaments, Category
from UserCenter.models import User


def populate():
    return None


if __name__ == '__main__':
    print('Starting rango population script...')
    populate()

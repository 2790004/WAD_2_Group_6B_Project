import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tournament.settings')

import django

django.setup()

from FilesManage.models import Pictures
from Teams.models import Teams, Team2User
from Tournaments.models import Tournaments, Category
from UserCenter.models import User as UserCenterUser
from django.contrib.auth.models import User as AdminUser


def populate():
    # Add primary users
    admins = [
        {'username': 'EasonZhang', 'password': 'abc123456', 'email': '123@123.com', 'is_superuser': True,
         'is_staff': True, 'is_active': True, 'date_joined': '2019-01-01 00:00:00', 'first_name': 'Eason',
         'last_name': 'Zhang'},
    ]
    users = [
        {'id': 1, 'user_name': 'messi', 'email': '123@123.com', 'password': 'abc123456', 'pronouns': 'his',
         'scoresaber': '123', 'skillser': '123', 'discord': '1234'},
        {'id': 2, 'user_name': 'ronaldo', 'email': '124@123.com', 'password': 'abc123456', 'pronouns': 'his',
         'scoresaber': '123', 'skillser': '123', 'discord': '1234'},
    ]
    tournament_categories = [
        {'id': 1, 'name': 'SUPA_League'}
    ]
    tournaments = [
        {'id': 1, 'name': 'SUPA', 'description': 'SUPA', 'max_entries': 12, 'start_time': '2019-01-01 00:00:00',
         'end_time': '2024-01-01 00:00:00', 'category_id': 1},
    ]

    for admin in admins:
        add_admin(admin)

    for user in users:
        add_user(user)



def add_admin(admin):
    add_ad = AdminUser.objects.get_or_create(username=admin['username'])[0]
    add_ad.password = admin['password']
    add_ad.email = admin['email']
    add_ad.is_superuser = admin['is_superuser']
    add_ad.is_staff = admin['is_staff']
    add_ad.is_active = admin['is_active']
    add_ad.date_joined = admin['date_joined']
    add_ad.first_name = admin['first_name']
    add_ad.last_name = admin['last_name']
    add_ad.save()
    return add_ad


def add_user(user):
    add_us = UserCenterUser.objects.get_or_create(id=user['id'])[0]
    add_us.user_name = user['user_name']
    add_us.email = user['email']
    add_us.password = user['password']
    add_us.pronouns = user['pronouns']
    add_us.scoresaber = user['scoresaber']
    add_us.skillser = user['skillser']
    add_us.discord = user['discord']
    add_us.save()
    return add_us


def add_team_user(team_user):
    add_tu = Team2User.objects.get_or_create(id=team_user['id'])[0]
    add_tu.active = team_user['active']
    add_tu.user_id = team_user['user_id']
    add_tu.team_id = team_user['team_id']
    add_tu.save()
    return add_tu


def add_team(team):
    add_t = Teams.objects.get_or_create(id=team['id'])[0]
    add_t.team_name = team['team_name']
    add_t.team_leader = team['team_leader']
    add_t.description = team['description']
    add_t.active = team['active']
    add_t.save()
    return add_t


def add_tournament_category(tournament_category):
    add_tc = Category.objects.get_or_create(id=tournament_category['id'])[0]
    add_tc.name = tournament_category['name']
    add_tc.save()
    return add_tc


def add_tournament(tournament):
    add_t = Tournaments.objects.get_or_create(id=tournament['id'])[0]
    add_t.name = tournament['name']
    add_t.description = tournament['description']
    add_t.max_entries = 12
    add_t.start_time = tournament['start_time']
    add_t.end_time = tournament['end_time']
    add_t.category_id = tournament['category_id']
    add_t.save()
    return add_t


if __name__ == '__main__':
    print('Starting rango population script...')
    populate()
    print('Finished!')

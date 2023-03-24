from django.db import models
from FilesManage.models import Pictures
from UserCenter.models import User
from Tournaments.models import Tournaments

from django.utils.html import format_html


# Create your models here.


# team to user
class Teams(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, verbose_name='Name')
    tournaments = models.ManyToManyField(to=Tournaments, blank=True, verbose_name='Tournaments')
    description = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Description')
    picture = models.ManyToManyField(to=Pictures, blank=True, verbose_name='Picture')
    team_leader = models.ForeignKey(related_name='team_leader', to=User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Team Leader')
    member = models.ManyToManyField(to=User, blank=True, verbose_name='Member', through='Team2User', through_fields=('team', 'user'), related_name='team_member')

    def display_tournaments(self):
        tournaments = self.tournaments.all()
        if tournaments:
            html = ''
            for i in tournaments:
                html += '{}<br>'.format(i.name)
            return format_html(html)
        else:
            return ''

    display_tournaments.short_description = "Tournaments"
    display_tournaments.allow_tags = True

    def display_name(self):
        return 'View'

    display_name.allow_tags = True

    def display_pictures(self):
        pictures = self.picture.all()
        if pictures:
            html = ''
            for i in pictures:
                html += '<images src="{}" style="max-hight:50px; max-width:50px;">'.format(i.picture.url)
            return format_html(html)
        else:
            return ''

    display_pictures.short_description = "Picture"
    display_pictures.allow_tags = True

    def display_member(self):
        member = self.member.all()
        if member:
            html = ''
            for i in member:
                html += '{}<br>'.format(i.__str__())
            return format_html(html)
        else:
            return ''

    display_member.short_description = "Member"
    display_member.allow_tags = True

    active = models.BooleanField(default=False, blank=False, null=False, verbose_name='Active',
                                 help_text='Select as Approved')

    class Meta:
        verbose_name = "Teams"
        verbose_name_plural = "Teams List"

    def __str__(self):
        return self.name


# team to user
class Team2User(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='To User', related_name='Team2User_user')
    team = models.ForeignKey(to=Teams, on_delete=models.CASCADE, verbose_name='To Team', related_name='Team2User_team')
    active = models.BooleanField(default=False, blank=False, null=False, verbose_name='Active', help_text='Select to become a team member')  # pending if user have join the team

    def team_leader(self):
        if self.team:
            return self.team.team_leader.user_name
        else:
            return ''

    class Meta:
        verbose_name = "Team's member"
        verbose_name_plural = "Team's member List"

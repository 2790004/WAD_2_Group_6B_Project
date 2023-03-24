from django.db import models
from FilesManage.models import Pictures
from django.utils.html import format_html


# Create your models here.

# User table
class User(models.Model):
    user_name = models.CharField(unique=True, max_length=512, null=False, blank=False, verbose_name='User Name')
    email = models.EmailField(unique=True, max_length=64, null=False, blank=False, verbose_name='Email')
    password = models.CharField(max_length=512, null=False, blank=False, verbose_name='Password')
    pronouns = models.CharField(max_length=512, null=True, blank=True, verbose_name='Pronouns')
    scoresaber = models.TextField(max_length=512, null=True, blank=True, verbose_name='Scoresaber')
    skillset = models.TextField(max_length=512, null=True, blank=True, verbose_name='Skillset')
    profile_picture = models.ManyToManyField(to=Pictures, blank=True, verbose_name='Profile Pictures')

    def display_name(self):
        return 'View'

    display_name.short_description = " "
    display_name.allow_tags = True
    def display_profile_picture(self):
        profile_pictures = self.profile_picture.all()
        if profile_pictures:
            html = ''
            for i in profile_pictures:
                html += '<images src="{}" style="max-width: 80px; max-height: 80px;">'.format(i.picture.url)

            return format_html(html)
        else:
            return ''

    display_profile_picture.short_description = "Profile Pictures"
    display_profile_picture.allow_tags = True

    discord = models.CharField(max_length=512, null=True, blank=True, verbose_name='Discord')

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User List"

    def __str__(self):
        return self.user_name + ' : ' + self.email

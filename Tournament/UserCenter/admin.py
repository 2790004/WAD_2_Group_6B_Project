from django.contrib import admin
from .models import User

# Register your models here.

admin.site.site_header = 'Tournament'
admin.site.site_title = 'Tournament'
admin.site.index_title = 'Tournament'


class UserAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'user_name', 'email', 'password', 'pronouns', 'scoresaber', 'skillset',
                    'display_profile_picture', 'discord', ]
    search_fields = ['display_name', 'user_name', 'email', 'user_name', 'email', 'password', 'pronouns', 'scoresaber',
                     'skillset', 'discord', ]
    list_per_page = 100


admin.site.register(User, UserAdmin)

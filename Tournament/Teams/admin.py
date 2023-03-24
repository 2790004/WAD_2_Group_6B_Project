from django.contrib import admin
from .models import Teams, Team2User


# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'display_tournaments', 'name', 'description', 'display_pictures', 'team_leader',
                    'display_member', 'active', ]
    search_fields = ['name', 'description', 'tournaments__name', 'team_leader_user_name', 'member___user_name',
                     'active', ]
    list_filter = ['tournaments', 'team_leader', 'active']
    list_per_page = 100


admin.site.register(Teams, TeamsAdmin)


class Team2UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'team', 'team_leader', 'active', ]
    search_fields = ['name', 'user__name', 'team__name']
    list_filter = ['active', 'team__team_leader', ]
    list_per_page = 100


admin.site.register(Team2User, Team2UserAdmin)

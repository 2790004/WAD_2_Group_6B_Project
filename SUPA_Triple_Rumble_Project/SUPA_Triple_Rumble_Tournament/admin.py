from django.contrib import admin
from SUPA_Triple_Rumble_Tournament.models import Team, TeamTournament, IndividualTournament


# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Team)
admin.site.register(TeamTournament)

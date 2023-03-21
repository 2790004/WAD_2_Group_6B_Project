from django.contrib import admin
from models import Tournaments, Category
# Register your models here.


class TournamentsAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name', 'display_category', 'max_entries', 'start_time', 'end_tIme', ]
    search_fields = ['name', 'category__name', 'max_entries', 'start_time', 'end_tIme', ]
    list_per_page = 100


admin.site.register(Tournaments, TournamentsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name']
    list_per_page = 100


admin.site.register(Category, CategoryAdmin)

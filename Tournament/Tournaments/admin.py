from django.contrib import admin
from .models import Tournaments, Category


# Register your models here.

class TournamentsAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name', 'display_picture', 'description', 'display_category', 'max_entries',
                    'start_time', 'end_time', ]
    search_fields = ['name', 'description', 'category__name', 'max_entries', 'start_time', 'end_time', ]
    list_per_page = 100


admin.site.register(Tournaments, TournamentsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name']
    list_per_page = 100


admin.site.register(Category, CategoryAdmin)

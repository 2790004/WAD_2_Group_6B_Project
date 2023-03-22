from django.contrib import admin
from models import Pictures

# Register your models here.


class PicturesAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'picture']
    list_per_page = 100


admin.site.register(Pictures, PicturesAdmin)

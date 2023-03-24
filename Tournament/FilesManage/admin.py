from django.contrib import admin
from .models import Pictures


# Register your models here.

# The following code is to display the picture in the admin page
class PicturesAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'picture']
    list_per_page = 100

admin.site.register(Pictures, PicturesAdmin)

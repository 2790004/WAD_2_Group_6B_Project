from django.db import models
from FilesManage.models import Pictures
from django.utils.html import format_html


# Create your models here.

# Tournament's Category
class Category(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, verbose_name='Name')

    def display_name(self):
        return 'View'

    display_name.short_description = " "
    display_name.allow_tags = True

    class Meta:
        verbose_name = "Tournament Category"
        verbose_name_plural = "Tournament Category List"

    def __str__(self):
        return self.name


# Tournament table
class Tournaments(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, verbose_name='Name')
    max_entries = models.IntegerField(null=False, blank=False, verbose_name='Max Entries')
    start_time = models.DateTimeField(null=False, blank=False, verbose_name='Start Time')
    end_time = models.DateTimeField(null=False, blank=False, verbose_name='End Time')
    picture = models.ForeignKey(on_delete=models.SET_NULL, to=Pictures, blank=True, null=True, verbose_name='Pictures')
    description = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Description')
    category = models.ForeignKey(blank=False, to=Category, verbose_name='Category', on_delete=models.CASCADE)

    def display_name(self):
        return 'View'

    display_name.allow_tags = True

    # display the picture
    def display_picture(self):
        if self.picture:
            return format_html(
                '<images src="{}" style="max-width:50px;max-height:50px;">'.format(self.picture.picture.url))
        else:
            return ''

    display_picture.short_description = "Pictures"
    display_picture.allow_tags = True

    def display_category(self):
        return self.category.name

    display_category.short_description = "Category"
    display_category.allow_tags = True

    class Meta:
        verbose_name = "Tournament's"
        verbose_name_plural = "Tournament's List"

    def __str__(self):
        return self.name

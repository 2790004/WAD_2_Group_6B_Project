from django.db import models


# Create your models here.

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


class Tournaments(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, verbose_name='Name')

    def display_name(self):
        return 'View'

    display_name.short_description = " "
    display_name.allow_tags = True

    category = models.ForeignKey(blank=False, to=Category, verbose_name='Category', on_delete=models.CASCADE)

    def display_category(self):
        return self.category.name

    display_category.short_description = "Category"
    display_category.allow_tags = True

    max_entries = models.IntegerField(null=False, blank=False, verbose_name='Max Entries')
    start_time = models.DateTimeField(null=False, blank=False, verbose_name='Start Time')
    end_tIme = models.DateTimeField(null=False, blank=False, verbose_name='End Time')

    class Meta:
        verbose_name = "Tournaments"
        verbose_name_plural = "Tournaments List"

    def __str__(self):
        return self.name

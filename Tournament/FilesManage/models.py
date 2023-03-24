from django.db import models
from django.utils.html import format_html
import uuid, os
from Tournament.settings import MEDIA_ROOT


# Create your models here.

class Pictures(models.Model):

    # Upload the file and rename it
    def path_and_rename(instance, filename):
        tmp = filename.split('.')
        if len(tmp) > 1:
            ext = tmp[-1]
        else:
            ext = 'jpg'
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        folder = 'image'
        if not os.path.exists(os.path.join(MEDIA_ROOT, folder)):
            os.makedirs(os.path.join(MEDIA_ROOT, folder))
        return os.path.join(folder, filename)

    picture = models.ImageField(upload_to=path_and_rename, max_length=1048576, null=False, blank=False,
                                verbose_name='Picture')

    def display_name(self):
        return format_html('<images src={} style="max-width:50px;max-hight:50px;">'.format(self.picture.url))

    display_name.short_description = " "

    def __str__(self):
        return self.picture.url

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Picture list"

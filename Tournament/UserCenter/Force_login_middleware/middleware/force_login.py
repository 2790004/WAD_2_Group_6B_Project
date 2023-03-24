import time

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from Tournament.settings import MEDIA_URL, STATIC_URL, admin_url_path
import re, time
from urllib.parse import quote, unquote
from django.http import QueryDict


# If the user is not logged in, redirect to the login page
class force_login(MiddlewareMixin):
    def process_request(self, request):

        current_path = request.path
        url_all_info = request.build_absolute_uri()
        if re.match('(/{})|(/{})|(/{})|(^/{})|(^/{})|(^/{})'.format(MEDIA_URL.strip('/'), STATIC_URL.strip('/'), admin_url_path, 'UserCenter', '$', 'About'), current_path):
            return None

        if '//' in current_path:
            url_all_info = url_all_info.replace(current_path, re.sub('/{2,}', '/', current_path))
            return redirect(url_all_info)

        if not request.session.get('is_authenticated'):
            return redirect('/UserCenter/login/')

        else:
            next_str = re.sub('^[^\?]+\?', '', url_all_info, re.I)
            next_get = QueryDict(next_str)
            next = next_get.get('next', '')
            if next and re.match('/{}'.format(admin_url_path), current_path):
                return redirect(unquote(next))

        return None

    def process_response(self, request, response):
        return response
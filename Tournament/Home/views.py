from django.shortcuts import render, HttpResponse
from get_base_context.base_context.base_context import base_context


# Create your views here.

# If there is an error in the home page, it will be displayed in the console and the Homepage shows an error message
def home(request):
    try:

        return render(request, 'Home/home.html', base_context(request))
    except Exception as e:
        print('home:{}'.format(e))
        return HttpResponse('Home Page Error')

import re
from django.shortcuts import render, HttpResponse, redirect
from get_base_context.base_context.base_context import base_context

from .forms import register_forms
from .models import User
from django.db.models import Q


# Create your views here.


# register
def register(request):
    try:
        is_authenticated = request.session.get('is_authenticated', None)
        if is_authenticated:
            return redirect('/UserCenter/profile/')

        if request.method == 'GET':
            base_context_dict = base_context(request)

            context = base_context_dict
            forms = register_forms()
            context['forms'] = forms
            return render(request, 'UserCenter/register.html', context=context)
        else:
            errors_message = ''
            post = request.POST
            password = post.get('password', '')
            repassword = post.get('repassword', '')
            if password != repassword:
                errors_message += 'Two Different Passwords！'

            email = post.get('email', '')
            if not re.search('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
                errors_message += 'Email Error！'

            files = request.FILES.getlist('profile_picture')
            print(files)
            forms = register_forms(data=post)
            if forms.is_valid() and not errors_message:
                new_data = forms.save()
                print(new_data)
                if new_data and files:
                    for f in files:
                        new_data.profile_picture.create(picture=f)
                return redirect('/UserCenter/login/')
            else:
                # print(forms.errors)
                base_context_dict = base_context(request)
                context = base_context_dict
                # forms = register_forms(initial=forms.cleaned_data)
                context['forms'] = forms

                context['errors_message'] = errors_message

                return render(request, 'UserCenter/register.html', context=context)

    except Exception as e:
        print('register:{}'.format(e))
        return HttpResponse('Register Failed')


# profile
def profile(request):
    is_authenticated = request.session.get('is_authenticated', None)
    if not is_authenticated:
        return redirect('/UserCenter/login/')
    try:
        user_id = request.session.get('user_id', '')
        if not user_id:
            return redirect('/UserCenter/login')
        usertmp_q = User.objects.filter(id=user_id)
        if usertmp_q:
            user = usertmp_q.first()
        else:
            return redirect('/UserCenter/login')
        pre_pic = [i.picture.name for i in user.profile_picture.all()]
        print('pre_pic', pre_pic)

        if request.method == 'GET':

            base_context_dict = base_context(request)
            context = base_context_dict
            forms = register_forms(instance=user)
            context['forms'] = forms

            return render(request, 'UserCenter/profile.html', context=context)
        else:
            errors_message = ''
            post = request.POST

            password = post.get('password', '')
            repassword = post.get('repassword', '')
            if password != repassword:
                errors_message += 'Two Different Passwords！'

            email = post.get('email', '')
            if not re.search('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
                errors_message += 'Email Error！'

            files = request.FILES.getlist('profile_picture')
            print(files)
            forms = register_forms(instance=user, data=post)
            if forms.is_valid() and not errors_message:
                new_data = forms.save()
                print(new_data)
                if new_data and files:
                    for f in files:
                        new_data.profile_picture.create(picture=f)
                elif pre_pic:
                    for f in pre_pic:
                        new_data.profile_picture.create(picture=f)
                return redirect('/UserCenter/login/')
            else:
                # print(forms.errors)
                base_context_dict = base_context(request)
                context = base_context_dict
                # forms = register_forms(initial=forms.cleaned_data)
                context['forms'] = forms

                context['errors_message'] = errors_message

                return render(request, 'UserCenter/profile.html', context=context)

    except Exception as e:
        print('profile:{}'.format(e))
        return HttpResponse('edit profile Failed')


# login
def login(request):
    is_authenticated = request.session.get('is_authenticated', None)
    if is_authenticated:
        return redirect('/UserCenter/profile/')
    try:
        if request.session.get('is_authenticated'):
            return redirect(request.META.get('HTTP_REFERER', '/'))

        if request.method == 'GET':
            base_context_dict = base_context(request)
            context = base_context_dict
            forms = register_forms()
            context['forms'] = forms
            return render(request, 'UserCenter/login.html', context=context)
        else:
            errors_message = ''
            post = request.POST

            user_name_mobil_phone = post.get('user_name_email', '')
            password = post.get('password', '')

            user_q = User.objects.filter(
                (Q(user_name__iexact=user_name_mobil_phone) | Q(email__iexact=user_name_mobil_phone)) &
                Q(password=password))
            if user_q:
                request.session['is_authenticated'] = True
                request.session['user_id'] = user_q.first().id

                return redirect('/')
            else:
                if not user_q:
                    errors_message += 'Incorrect Username Or Password!'
                base_context_dict = base_context(request)
                context = base_context_dict
                forms = register_forms()
                context['forms'] = forms

                context['errors_message'] = errors_message

                return render(request, 'UserCenter/login.html', context=context)

    except Exception as e:
        print('login:{}'.format(e))
        return HttpResponse('Login Failed')


# logout
def sign_out(request):
    try:
        request.session['is_authenticated'] = False
        return redirect('/')

    except Exception as e:
        print('sign_out:{}'.format(e))
        return HttpResponse('Sign Out Error!')

from Tournament.settings import admin_url_path, STATIC_URL
from UserCenter.models import User


# get the base context to be used in all pages
def base_context(request):
    try:
        is_authenticated = request.session.get('is_authenticated', None)
        if is_authenticated:
            user_q = User.objects.filter(id=request.session.get('user_id', None))
            user_name = user_q.first().user_name
            email = user_q.first().email
            profile_picture_tmp = user_q.first().profile_picture.all()
            if profile_picture_tmp:
                user_picture = profile_picture_tmp.first().picture.url
            else:
                user_picture = STATIC_URL + 'images/' + 'noname.png'
        sign_out = '/UserCenter/sign_out/'
        admin_url = '/{}/'.format(admin_url_path)
        current_path = request.build_absolute_uri()
        return locals()
    except Exception as e:
        print('base_context:{}'.format(e))
        return {}
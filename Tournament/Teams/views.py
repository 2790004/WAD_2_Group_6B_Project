from django.shortcuts import render, HttpResponse, redirect
from get_base_context.base_context.base_context import base_context
from Tournaments.models import Tournaments
from Teams.models import Teams, Team2User, User
from django.template.loader import render_to_string
from django.db.models import Q
from .forms import create_team_get, create_team_post
from django.http import QueryDict
# Create your views here.

#队伍列表页
def list(request):
    try:
        tournaments = Tournaments.objects.all()
        return render(request, 'Team/list.html', {**locals(), **base_context(request)})
    except Exception as e:
        print('home:{}'.format(e))
        return HttpResponse('Team List Page Error')

#点击tournament ajax 获取其下的teams
def from_tournament_get_team_list(request):
    try:
        if request.method == 'GET':
            return HttpResponse('please use POST method')
        tournament_id = request.POST.get('id', '')
        if not tournament_id:
            return HttpResponse('not tournament_id')

        teams = []
        teams_tmp = Teams.objects.filter(Q(tournaments__id=tournament_id) & Q(active=True))
        if teams_tmp:
            for i in teams_tmp:
                i.team2user = Team2User.objects.filter(Q(team_id=i.id) & Q(active=True))
                teams.append(i)


        print('teams', teams)
        if teams:
            html = render_to_string('Team/from_tournament_get_team_list.html', {**locals(), **base_context(request)}, request)
        else:
            html = ''
        return HttpResponse(html)
    except Exception as e:
        print('home:{}'.format(e))
        return HttpResponse('from_tournament_get_team_list Error')

#我是队伍创建人的时候，管理队成员
def manage_team(request):
    try:
        user_id = request.session['user_id']
        if not user_id:
            return HttpResponse('not user')

        teams = []
        team_tmp = Teams.objects.filter(team_leader_id=user_id)
        print('team_tmp', team_tmp)
        if team_tmp:
            for i in team_tmp:
                i.team2user = Team2User.objects.filter(team_id=i.id)
                print(i.team2user)
                teams.append(i)

        return render(request, 'Team/manage_team.html', {**locals(), **base_context(request)})
    except Exception as e:
        print('manage_team:{}'.format(e))
        return HttpResponse('manage_team Error')

#创建队伍
def create_team(request):
    try:
        user_id = request.session['user_id']
        if not user_id:
            return HttpResponse('not user')
        if request.method == 'GET':
            forms = create_team_get()
            return render(request, 'Team/create_team.html', {**locals(), **base_context(request)})
        else:
            data = request.POST.copy()
            data.setdefault('team_leader', user_id)
            forms = create_team_post(data=data)
            files = request.FILES.getlist('picture')
            if forms.is_valid():
                new_data = forms.save()
                print(new_data)
                if new_data and files:
                    for f in files:
                        new_data.picture.create(picture=f)
                return redirect('/Teams/manage_team/')
            else:
                errors_message = 'Error, please reinput.'
                forms = create_team_get(data=request.POST)
                return render(request, 'Team/create_team.html', {**locals(), **base_context(request)})
    except Exception as e:
        print('create_team:{}'.format(e))
        return HttpResponse('create_team Error')

#同意成员入队
def agree_user_join_team(request):
    try:
        user_id = request.session['user_id']
        team_id = request.POST.get('team_id', '')
        applicant_id = request.POST.get('applicant_id', '')
        if not user_id or not team_id or not applicant_id:
            return HttpResponse('user team applicant error')

        actions = Team2User.objects.filter(Q(team__team_leader_id=user_id) & Q(team_id=team_id) & Q(user_id=applicant_id) & Q(active=False))
        print('actions', actions)
        if actions:
            c_actions = actions.first()
            c_actions.active = True
            c_actions.save()
            print('actions.first().active', c_actions.active)
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    except Exception as e:
        print('agree_user_join_team:{}'.format(e))
        return HttpResponse('agree_user_join_team Error')

#移除队伍成员
def from_team_remove_user(request):
    try:
        user_id = request.session['user_id']
        team_id = request.POST.get('team_id', '')
        applicant_id = request.POST.get('applicant_id', '')
        if not user_id or not team_id or not applicant_id:
            return HttpResponse('user team applicant error')

        actions = Team2User.objects.filter(Q(team__team_leader_id=user_id) & Q(team_id=team_id) & Q(user_id=applicant_id) & Q(active=True))
        print('actions', actions)
        if actions:
            actions.delete()
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    except Exception as e:
        print('from_team_remove_user:{}'.format(e))
        return HttpResponse('from_team_remove_user Error')

#用户申请加入某队
def join_exit_team(request):
    try:
        user_id = request.session['user_id']
        teams = []
        teams_tmp = Teams.objects.filter(~Q(team_leader_id=user_id))
        for i in teams_tmp:
            team_id = i.id
            joined_state = Team2User.objects.filter(team_id=team_id, user_id=user_id)
            print('joined_state', joined_state)
            if joined_state:
                i.joined_state = True
            else:
                i.joined_state = False
            teams.append(i)


        return render(request, 'Team/join_exit_team.html', {**locals(), **base_context(request)})
    except Exception as e:
        print('join_exit_team:{}'.format(e))
        return HttpResponse('join_exit_team Error')

#入队退队ajax请求
def chang_join_state(request):
    if request.method == 'GET':
        return HttpResponse('please use POST method')

    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    team_id = request.POST.get('team_id', '')
    join_state = request.POST.get('join_state', '')
    if not join_state or not team_id or not user_id:
        return HttpResponse('not join_state or not team_id or not user_id')

    team_id = team_id.lstrip('id-')
    print(join_state, team_id, user_id)

    if join_state == 'false':#申请加入
        team_q = Teams.objects.filter(Q(id=team_id) & ~Q(team_leader__id=user_id) & ~Q(member__id=user_id))
        if team_q:
            team = team_q.first()
            team.member.add(user)
            return HttpResponse('1')
    elif join_state == 'true':#申请退出
        team_q = Team2User.objects.filter(Q(team_id=team_id) & Q(user_id=user_id))
        if team_q:
            team_q.delete()
            return HttpResponse('1')

    return HttpResponse('unknown')


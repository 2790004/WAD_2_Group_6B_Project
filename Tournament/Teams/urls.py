from django.urls import path, re_path, include
from . import views



urlpatterns = [


    path('from_tournament_get_team_list/', views.from_tournament_get_team_list, name='from_tournament_get_team_list'),#点击tournament ajax 获取其下的teams
    path('chang_join_state/', views.chang_join_state, name='chang_join_state'),#入队退队ajax请求
    path('manage_team/', views.manage_team, name='manage_team'),#我是队伍创建人的时候，管理队成员
    path('create_team/', views.create_team, name='create_team'),#创建队伍
    path('from_team_remove_user/', views.from_team_remove_user, name='from_team_remove_user'),#移除队伍成员
    path('agree_user_join_team/', views.agree_user_join_team, name='agree_user_join_team'),#同意成员入队
    path('join_exit_team/', views.join_exit_team, name='join_exit_team'),#用户申请加入某队
    re_path('.*', views.list, name='list'),#队伍列表页


]
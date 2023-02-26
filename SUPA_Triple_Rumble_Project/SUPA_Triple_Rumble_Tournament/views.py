from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Index.")


def about(request):
    return HttpResponse("About.")


def staff(request):
    return HttpResponse("Staff.")


def profile(request):
    return HttpResponse("Profile.")


def staff_profile(request):
    return HttpResponse("Staff Profile.")


def login(request):
    return HttpResponse("Login.")


def sign_up(request):
    return HttpResponse("Sign up.")


def teams(request):
    return HttpResponse("Teams")


def create_team(request):
    return HttpResponse("Create a team.")


def tournaments(request):
    return HttpResponse("Tournament.")


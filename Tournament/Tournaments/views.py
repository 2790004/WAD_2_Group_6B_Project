from django.shortcuts import render
from .models import Tournaments
from Teams.models import Teams
from get_base_context.base_context.base_context import base_context


# Create your views here.

# Tournament list page
def index(request):
    id = request.GET.get('id', '')
    if id:
        tournaments = Tournaments.objects.filter(id=id)
    else:
        tournaments = Tournaments.objects.all()
    if tournaments:
        for i in tournaments:
            i.used_entries = len(Teams.objects.filter(tournaments__id=i.id))
    return render(request, 'Tournaments/index.html', {**locals(), **base_context(request)})
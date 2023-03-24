from django import forms
from . import models
from django.forms import widgets as wid
from django.core.exceptions import ValidationError
import re


# create the team without data
class create_team_get(forms.ModelForm):
    class Meta:
        model = models.Teams
        fields = "__all__"
        exclude = ['team_leader', 'member', 'active']

        widgets = {
            'tournaments': wid.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'select tournaments'}),
            'name': wid.TextInput(attrs={'class': 'form-control', 'placeholder': 'team\'s name'}),
            'description': wid.Textarea(attrs={'class': 'form-control', 'placeholder': 'team\'s description'}),
            'picture': wid.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'team\'s picture'}),

        }


# create the team with data
class create_team_post(forms.ModelForm):
    class Meta:
        model = models.Teams
        fields = "__all__"

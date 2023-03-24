from django import forms
from . import models
from django.forms import widgets as wid


# User register
class register_forms(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"
        widgets = {
            'user_name': wid.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            'email': wid.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': wid.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'pronouns': wid.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pronouns'}),
            'scoresaber': wid.Textarea(attrs={'class': 'form-control', 'placeholder': 'Scoresaber', 'rows': "5"}),
            'skillset': wid.Textarea(attrs={'class': 'form-control', 'placeholder': 'Skillset', 'rows': "5"}),
            'profile_picture': wid.ClearableFileInput(
                attrs={'class': 'form-control', 'multiple': 'multiple', 'accept': 'image/*'}),
            'discord': wid.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discord'}),
        }

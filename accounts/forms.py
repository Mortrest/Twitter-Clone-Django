from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TweetForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'body'
        ]

from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TweetForm(ModelForm):

    class Meta:
        model = Post
        widgets = {
                'body': forms.Textarea(attrs={
                'class':'form-control',
                'style':'background-color:#202a34;border:none;color: rgb(216, 205, 186); font-size: 17px;font-family:inherit;font-weight: 600;height:56px;placeholder:"hello";width:58em;resize:none;',
                'placeholder':"What's happening?"
            },)
        }
        fields = [
            'body'
        ]


class TweetForm2(ModelForm):

    class Meta:
        model = Post
        widgets = {
                'body': forms.TextInput(attrs={
                'class':'form-control no-outline',
                'style':'background-color:#202a34;border:none;color: rgb(216, 205, 186); font-size: 15px;font-family:inherit;font-weight: 600;height:40px;placeholder:"hello";width:40em;resize:none;',
                'placeholder':"What's happening?",
                'outline':'none',
            },)
        }
        fields = [
            'body'
        ]


        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username','email', 'password1','password2'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class':'form-control',
                'style':'background-color:#202a34;border:none;color: rgb(216, 205, 186); font-size: 18px;font-family:inherit;font-weight: 600;'
            },)
        }
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

from django import forms
from .models import Post


class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'authors',
            'categorys',
            'theme_news',
            'body_news',
        ]


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='Common')
        basic_group.user_set.add(user)
        return user

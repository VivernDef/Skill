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

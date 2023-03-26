from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import *
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy



class Author (models.Model):
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rate = models.FloatField(default=0.0)

    def __str__(self):
        return f'Name: {self.user_auth.username}'


class Category (models.Model):
    theme = models.CharField(max_length=100, unique = True, help_text=_('thm cat'))
    subscribers = models.ManyToManyField(User, blank= True, null= True, related_name='categories_sub' )

    def __str__(self):
        return self.theme


class Post (models.Model):
    article = 'AE'
    news = 'NS'
    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]

    authors = models.ForeignKey(Author, on_delete = models.CASCADE, related_name='posts', verbose_name=pgettext_lazy('this text for help', 'author name is'))

    choice_news = models.CharField(max_length=2, choices = POSITIONS, default=news)

    date_joined = models.DateTimeField(('date joined'), auto_now_add = True,)

    categorys = models.ManyToManyField(Category, through='PostCategory')

    theme_news = models.CharField(max_length=100, unique=True,)

    body_news = models.TextField(max_length=None)

    rate_news = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return f'/news/{self.id}'
       # return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rate_news += 1
        self.save()

    def dislike(self):
        self.rate_news -= 1
        self.save()

    def preview(self):
        return f'{self.body_news[0:124]}...'

    def __str__(self):
        return f'{self.theme_news.title()}: {self.body_news[:20]}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    commenter_user = models.ForeignKey(User, on_delete= models.CASCADE)

    comments = models.TextField(max_length=None)

    date_joined_comm = models.DateTimeField(('date joined'), auto_now_add = True)

    rate_comm = models.FloatField(default=0.0)

    def like(self):
        self.rate_comm += 1
        self.save()

    def dislike(self):
        self.rate_comm -= 1
        self.save()

    def __str__(self):
        return self.comments

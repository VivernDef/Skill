from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import *


class Author (models.Model):
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rate = models.FloatField(default=0.0)


class Category (models.Model):
    theme = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.theme.title()


class Post (models.Model):
    article = 'AE'
    news = 'NS'
    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]

    authors = models.ForeignKey(Author, on_delete = models.RESTRICT, related_name='posts')

    choice_news = models.CharField(max_length=2, choices = POSITIONS, default=news)

    date_joined = models.DateTimeField(('date joined'), auto_now_add = True,)

    categorys = models.ManyToManyField(Category, through='PostCategory')

    theme_news = models.CharField(max_length=100, unique=True)

    body_news = models.TextField(max_length=None)

    rate_news = models.FloatField(default=0.0)

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
    post = models.ForeignKey(Post, on_delete= models.RESTRICT)
    category = models.ForeignKey(Category, on_delete= models.RESTRICT)


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.RESTRICT, related_name='comments')

    commenter_user = models.ForeignKey(User, on_delete= models.RESTRICT)

    comments = models.TextField(max_length=None)

    date_joined_comm = models.DateTimeField(('date joined'), auto_now_add = True)

    rate_comm = models.FloatField(default=0.0)

    def like(self):
        self.rate_comm += 1
        self.save()

    def dislike(self):
        self.rate_comm -= 1
        self.save()
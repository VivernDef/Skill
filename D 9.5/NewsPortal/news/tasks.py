import time
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import datetime

from news.models import Category, Post


@shared_task
def send_notifications(preview, pk, theme_news, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=theme_news,
        body='',
        from_email='send.testmail',
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekstart_send():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_joined__gte=last_week)
    categories = set(posts.values_list('category__theme', flat=True))
    subscribers = set(Category.objects.filter(theme__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'week_send.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email='send.testmail',
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

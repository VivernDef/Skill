from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string


from NewsPortal import settings
from news.models import PostCategory


def send_notifications(preview, pk, theme_news, subscribers):
    html_content = render_to_string(
        'post_created_mail.html',
        {
            'text': preview,
            'link': f'{ settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=theme_news,
        body='',
        from_email='send.testmail@yandex.ru',
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def send_mail(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categorys.all()
        subscribers_email = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_email += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.theme_news, subscribers_email )


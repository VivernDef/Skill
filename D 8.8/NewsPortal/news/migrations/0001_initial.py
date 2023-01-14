# Generated by Django 4.1.3 on 2022-11-21 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rate', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_news', models.CharField(choices=[('AE', 'Статья'), ('NS', 'Новость')], default='NS', max_length=2)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('theme_news', models.CharField(max_length=100, unique=True)),
                ('body_news', models.TextField()),
                ('rate_news', models.FloatField(default=0.0)),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='news.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categorys',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('date_joined_comm', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('rate_comm', models.FloatField(default=0.0)),
                ('commenter_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='news.post')),
            ],
        ),
    ]
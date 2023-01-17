# Generated by Django 4.1.1 on 2022-12-03 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='comments', to='news.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='posts', to='news.author'),
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-09 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contactform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertteam',
            name='email',
        ),
        migrations.RemoveField(
            model_name='expertteam',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='expertteam',
            name='position',
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_images_projext_alter_expertteam_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertteam',
            name='twitter',
        ),
        migrations.AddField(
            model_name='expertteam',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 5.0.4 on 2024-10-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='siteedit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('domain', models.CharField(blank=True, default=models.CharField(blank=True, max_length=50, null=True), max_length=50, null=True)),
                ('Address', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('dis', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.TextField(blank=True, null=True)),
                ('image1', models.TextField(blank=True, null=True)),
                ('idx', models.IntegerField(default=1)),
            ],
        ),
    ]

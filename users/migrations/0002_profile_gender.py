# Generated by Django 3.2 on 2021-12-22 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='Unspecified', max_length=12),
        ),
    ]

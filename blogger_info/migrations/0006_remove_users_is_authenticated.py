# Generated by Django 4.2 on 2023-04-16 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger_info', '0005_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_authenticated',
        ),
    ]
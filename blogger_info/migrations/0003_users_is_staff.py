# Generated by Django 4.2 on 2023-04-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger_info', '0002_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
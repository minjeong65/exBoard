# Generated by Django 3.2.8 on 2021-10-29 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_user_coment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='coment',
            new_name='comment',
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='post')),
            ],
        ),
    ]
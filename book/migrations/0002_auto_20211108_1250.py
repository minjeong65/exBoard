# Generated by Django 3.2.8 on 2021-11-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=30)),
                ('site_url', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

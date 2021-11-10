# Generated by Django 3.2.8 on 2021-11-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_site_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='site_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='site_url',
            field=models.TextField(),
        ),
    ]
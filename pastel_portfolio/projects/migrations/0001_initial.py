# Generated by Django 3.2.3 on 2021-09-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Porjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=200)),
                ('image', models.FilePathField(path='./static/img')),
                ('tec_key', models.CharField(max_length=100)),
                ('header', models.CharField(max_length=200)),
                ('para', models.TextField(max_length=3000)),
            ],
        ),
    ]
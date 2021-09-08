# Generated by Django 3.2.7 on 2021-09-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=200)),
                ('image', models.FilePathField(path='./static/img')),
                ('keys', models.CharField(max_length=100)),
                ('header', models.CharField(max_length=200)),
                ('para', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='porjects',
            old_name='brief',
            new_name='subheader',
        ),
        migrations.RenameField(
            model_name='porjects',
            old_name='tec_key',
            new_name='tech',
        ),
        migrations.AlterField(
            model_name='porjects',
            name='para',
            field=models.TextField(),
        ),
    ]
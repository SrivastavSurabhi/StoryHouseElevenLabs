# Generated by Django 4.2.2 on 2023-06-27 10:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textToSpeech', '0015_html_parent_file_alter_epub_upload_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epub',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 15, 31, 20, 826026)),
        ),
        migrations.AlterField(
            model_name='html',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 15, 31, 20, 827025)),
        ),
        migrations.AlterField(
            model_name='mp3',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 15, 31, 20, 827025)),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 15, 31, 20, 825028)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 27, 15, 31, 20, 827025)),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('path', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('upload_on', models.DateTimeField(default=datetime.datetime(2023, 6, 27, 15, 31, 20, 826026))),
                ('is_public', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

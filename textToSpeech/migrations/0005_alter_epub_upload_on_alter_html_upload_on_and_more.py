# Generated by Django 4.2 on 2023-05-05 13:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textToSpeech', '0004_alter_epub_upload_on_alter_pdf_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epub',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 18, 35, 49, 79729)),
        ),
        migrations.AlterField(
            model_name='html',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 18, 35, 49, 80726)),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 18, 35, 49, 78726)),
        ),
        migrations.CreateModel(
            name='MP3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('path', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('upload_on', models.DateTimeField(default=datetime.datetime(2023, 5, 5, 18, 35, 49, 81729))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
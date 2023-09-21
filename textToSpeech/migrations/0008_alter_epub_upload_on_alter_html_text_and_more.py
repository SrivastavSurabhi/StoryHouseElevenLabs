# Generated by Django 4.2 on 2023-05-09 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textToSpeech', '0007_summary_text_alter_epub_name_alter_epub_upload_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epub',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 10, 54, 30, 867396)),
        ),
        migrations.AlterField(
            model_name='html',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='html',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 10, 54, 30, 868395)),
        ),
        migrations.AlterField(
            model_name='mp3',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 10, 54, 30, 870398)),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 10, 54, 30, 866393)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 10, 54, 30, 871397)),
        ),
    ]

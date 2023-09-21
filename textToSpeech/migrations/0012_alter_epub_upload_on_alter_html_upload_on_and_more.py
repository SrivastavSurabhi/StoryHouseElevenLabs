# Generated by Django 4.2 on 2023-05-18 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textToSpeech', '0011_epub_is_public_html_is_public_pdf_is_public_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epub',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 15, 12, 41, 450036)),
        ),
        migrations.AlterField(
            model_name='html',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 15, 12, 41, 450036)),
        ),
        migrations.AlterField(
            model_name='mp3',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 15, 12, 41, 451033)),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 15, 12, 41, 449033)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 15, 12, 41, 452033)),
        ),
    ]
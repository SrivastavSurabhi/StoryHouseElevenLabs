# Generated by Django 4.2 on 2023-06-13 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textToSpeech', '0014_alter_epub_upload_on_alter_html_upload_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='html',
            name='parent_file',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='epub',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 16, 53, 0, 682899)),
        ),
        migrations.AlterField(
            model_name='html',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 16, 53, 0, 682899)),
        ),
        migrations.AlterField(
            model_name='mp3',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 16, 53, 0, 683897)),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 16, 53, 0, 681898)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='upload_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 16, 53, 0, 684898)),
        ),
    ]

# Generated by Django 4.2 on 2023-05-02 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_passwordreset_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 18, 26, 52, 822502), editable=False),
        ),
    ]
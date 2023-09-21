from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class PDF(models.Model):
    name = models.CharField(max_length=80)
    path = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=False)
    upload_on = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)


class Text(models.Model):
    name = models.CharField(max_length=80)
    path = models.CharField(max_length=100, blank=True)
    text = models.TextField(null=True, blank=True)
    total_charachter = models.IntegerField(default=0)
    text_to_speech_status = models.BooleanField(default=False)
    summary_status = models.BooleanField(default=False)
    upload_on = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    parent_file = models.CharField(max_length=1000, null=True, blank=True)


class EPUB(models.Model):
    name = models.CharField(max_length=80)
    path = models.CharField(max_length=100, blank=True, unique=True)
    status = models.BooleanField(default=False)
    upload_on = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)


class HTML(models.Model):
    name = models.CharField(max_length=80)
    path = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    text_to_speech_status = models.BooleanField(default=False)
    summary_status = models.BooleanField(default=False)
    upload_on = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    parent_file = models.CharField(max_length=1000)


class MP3(models.Model):
    name = models.CharField(max_length=80)
    path = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=False)
    upload_on = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Summary(models.Model):
    name = models.CharField(max_length=80)
    path = models.CharField(max_length=100, blank=True)
    upload_on = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

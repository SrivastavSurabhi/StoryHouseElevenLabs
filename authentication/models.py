from django.db import models
import uuid
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="userprofile/")


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    is_used = models.BooleanField(default=False)
    expires = models.DateTimeField(editable=False, default=datetime.now()+timedelta(days=1))



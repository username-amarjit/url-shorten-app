from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class URL(models.Model):
    id = models.AutoField(primary_key=True)
    long_url = models.URLField(max_length=200,db_index=True)
    short_url_key = models.CharField(max_length=50, unique=True,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=30))
    
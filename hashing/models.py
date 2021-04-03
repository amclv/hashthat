from django.db import models

class Hash(models.Model):
    text = models.TextField()
    # SHA256 is always 64 characters long
    hash = models.CharField(max_length=64)
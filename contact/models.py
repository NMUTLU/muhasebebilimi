from django.db import models

# Create your models here.
class Contact (models.Model):
    isminiz = models.CharField(max_length=30)
    notunuz = models.TextField()
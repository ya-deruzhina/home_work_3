from django.db import models

# Create your models here.
class News (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    description = models.TextField(default ='')
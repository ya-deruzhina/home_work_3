from django.db import models
from flask import Flask, request
import psycopg2

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    counter = models.PositiveIntegerField(default=0)
from django.db import models
from flask import Flask, request
import psycopg2
from django.dispatch import receiver
from django.db.models.signals import pre_save

#Максимальное количество элементов
MAX_ELEMENTS = {'home' : 20, 'cat' : 40}

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    counter = models.PositiveIntegerField(default=0)
    category = models.TextField(default='None')
    date_create = models.DateTimeField(auto_now_add = True)


@receiver (pre_save, sender=Post)
def my_handler(sender, instance, **kwargs):
    if Post.objects.filter(category=instance.category).count()>=MAX_ELEMENTS.get(instance.category, 10):
        Post.objects.filter(category=instance.category).order_by('date_create').first().delete()
    print ('deleted')


class Comment (models.Model):
    text = models.CharField()
    new = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    status = models.CharField()

class Wallet (models.Model):
    name = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    balance = models.FloatField(default=0)
    
    def serilize_from_db (self):
        return {'name':self.name, 'currency':self.currency, 'balance': self.balance}

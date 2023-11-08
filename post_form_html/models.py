from django.db import models
# from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class PostForm (models.Model):
    title = models.CharField(max_length=100)
    text = RichTextField(blank=True, null=True)
    counter = models.PositiveIntegerField(default=0)
    category = models.TextField(default='None')
    date_create = models.DateTimeField(auto_now_add = True)

class CommentForm (models.Model):
    text = models.CharField()
    new = models.ForeignKey(PostForm, on_delete=models.CASCADE, related_name = 'comments')
    status = models.CharField()

    # def __str__(self):
    #     return self.text

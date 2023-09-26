from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import models
from .models import Post
import json
from django.views.decorators.csrf import csrf_exempt


POSTS = [
    {
        'id':'0',
        'title': 'first post',
        'text':'post1'
    },
    {
        'id':'2',
        'title': 'second post',
        'text':'post2'
    },
    {
        'id':'3',
        'title': 'last post',
        'text':'post3'
    }
]


# Create your views here.
def get_post_first(request):
    text_post = []
    for post in POSTS:
        text_post.append(post)
    return JsonResponse(text_post,safe=False)

#Выводит все посты
def get_posts(request):
    text_post = {
        'Posts':[]
    }
    posts = Post.objects.all()
    for post in posts:
        text_post['Posts'].append({'id':post.id, 'title':post.title,'text':post.text})
    return JsonResponse(text_post)

#Выводит пост по id(те, которые записаны в базе)    
def get_post(request, post_id):
    post = Post.objects.get(id= post_id)
    return JsonResponse ({'id':post_id,'title':post.title,'text':post.text})

# Создает новый пост  // запрос POST - Body - Raw - Json!!!!
@csrf_exempt
def create_post(request):
    title_1 = json.loads(request.body.decode('utf-8')).get('title')
    text_1 = json.loads(request.body.decode('utf-8')).get('text')
    post = Post(title=title_1, text=text_1)
    post.save()    
    return JsonResponse ({"Message":"Post Created"})

#Создание поста по заранее заданным данным
# def create_post(request):
#     post = Post(title='New Post', text='New Text')
#     post.save()
#     return JsonResponse({})




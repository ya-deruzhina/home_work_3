from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import models
from .models import Post
import json
from django.views.decorators.csrf import csrf_exempt


#Для красивого вывода данных:
def parse_posts(post: Post):
    return {'id':post.id, 'title':post.title,'text':post.text, 'counter':post.counter}

#Выводит все посты и считает их количество 
def get_all_posts(request):
    all_posts = {
        'Posts':[]
    }
    posts = Post.objects.all().order_by('id')
    for post in posts:
        all_posts['Posts'].append(parse_posts(post))
    all_posts['count'] = posts.count()
    return JsonResponse(all_posts)

#Выводит пост по id(те, которые записаны в базе) или "Not Created"    
#ToDo: сделать фильтр по id.
def post_by_id (request, post_id):
    id_by_post = Post.objects.filter(id=post_id)
    if len(id_by_post) !=0:
        post = Post.objects.get(id= post_id)    
        return JsonResponse (parse_posts(post))
    else:
        return JsonResponse ({"Status":"Not Created"})   


#Выводит пост по counter (те, которые записаны в базе) или "Not Created"    
#ToDo: сделать фильтр по id.
def post_by_counter (request, count):
    counter_posts = {
        'Posts':[]
    }
    count_by_post = Post.objects.filter(counter=count)
    if len(count_by_post) !=0:
        for post in count_by_post:
            counter_posts['Posts'].append(parse_posts(post))    
        return JsonResponse (counter_posts)
    else:
        return JsonResponse ({"Status":"Not Created"})   


# Исключает данные по параметру id=post_id
#ToDo: сделать фильтр по id.
def post_exept_id(request,post_id):
    posts_exept_id = {
        'Posts':[],
    }
    posts = Post.objects.all()
    for post in posts.exclude(id=post_id):
        posts_exept_id['Posts'].append(parse_posts(post))
    return JsonResponse(posts_exept_id)

# Исключает данные по параметру counter=count
#ToDo: сделать фильтр по id.
def post_exept_counter(request,count):
    posts_exept_counter = {
        'Posts':[],
    }
    posts = Post.objects.all()
    for post in posts.exclude(counter=count):
        posts_exept_counter['Posts'].append(parse_posts(post))
    return JsonResponse(posts_exept_counter)


#Создает (если не создан) пост по введенным данным 
# (POST - Body - form-data)
@csrf_exempt
def create_post(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    text = request.POST.get('text')
    counter = request.POST.get('counter')
    # category = request.POST.get('category')
    # date_create = request.POST.get('date_create')
    post, is_created = Post.objects.get_or_create(id=id,title=title, text=text,counter=counter)
    return JsonResponse (parse_posts(post))


#Меняет данные по id
# @csrf_exempt
# def update_post(request,post_id):
#     post = Post.objects.get(id=post_id)
#     post.title = json.loads(request.body.decode('utf-8')).get('title')
#     post.text = json.loads(request.body.decode('utf-8')).get('text')
#     post.counter = json.loads(request.body.decode('utf-8')).get('counter')
#     if post.title != None  and post.text != None and post.counter != None:
#         post.save(update_fields=["title","text","counter"])
#         return JsonResponse ({"Status":"Update"})
#     else:
#         return JsonResponse ({"Status":"Not Update, Not Found"})

#Меняет данные по id
# @csrf_exempt
# def update_post(request,post_id):
#     post = Post.objects.get(id=post_id)
#     update_dict = {}
#     post.title = json.loads(request.body.decode('utf-8')).get('title')
#     update_dict['title'] = post.title
#     post.text = json.loads(request.body.decode('utf-8')).get('text')
#     update_dict['text'] = post.text
#     post.counter = json.loads(request.body.decode('utf-8')).get('counter')
#     update_dict['counter'] = post.counter
#     inv_d = dict(filter(lambda x: x[1] is not None, update_dict.items()))
#     keys_by_update = list(inv_d.keys())
#     if len(keys_by_update) !=0:
#         post.save(update_fields=keys_by_update)
#         return JsonResponse ({"Status":"Update"})
#     else:
#         return JsonResponse ({"Status":"Not Update, Not Found"})

@csrf_exempt
def update_post(request,post_id):
    ALLOWED_FIELDS = ['title', 'text', 'counter']
    post = Post.objects.get(id=post_id)
    request_payload = json.loads(request.body.decode('utf-8'))
    for request_payload_field_key, request_payload_field_value in request_payload.items():
        if request_payload_field_key not in ALLOWED_FIELDS:
            continue
        setattr(post, request_payload_field_key, request_payload_field_value)
    post.save()
    return JsonResponse ({"Status":"Update"})
 

#Удалить пост по id
def delete_post(request, post_id):
    id_by_post = Post.objects.filter(id=post_id)
    if len(id_by_post) !=0:
        post = Post.objects.get(id=post_id)
        post.delete() 
        return JsonResponse ({"Status":"Deleted"})
    else:
        return JsonResponse ({"Status":"Not Created"})






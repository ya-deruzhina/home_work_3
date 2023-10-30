# Здесь будут операции с постами: вывод по id, создание, редактирование, удаление
from posts.models import Post
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest,HttpResponseRedirect
from posts.models import Wallet
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.template import loader

class PostView(View):
    @staticmethod
    #Для красивого вывода данных:
    def parse_posts(post: Post):
        return {'id':post.id, 'title':post.title,'text':post.text, 'counter':post.counter}

    #Выводит пост по id(те, которые записаны в базе) или "Not Created"    
    #ToDo: сделать фильтр по id.
    def get (self,request, post_id, *args,**kwargs):
        id_by_post = Post.objects.filter(id=post_id)
        if len(id_by_post) !=0:
            post = Post.objects.get(id= post_id)    
            template = loader.get_template("post_and_comments/view_post.html")
            context = {
            "post":post,
        }
            return HttpResponse(template.render(context,request))
        else:
            return JsonResponse ({"Status":"Not Created"}) 

    
    #Меняет данные
    @csrf_exempt
    def post(self,request, post_id,*args,**kwargs):
        post = Post.objects.get(id=post_id)
        request_payload = {}
        post.title = request.POST.get('title')
        request_payload['title'] = post.title
        post.text = request.POST.get('text')
        request_payload['text'] = post.text
        post.counter = request.POST.get('counter')
        request_payload['counter'] = post.counter
        inv_d = dict(filter(lambda x: x[1] is not '' , request_payload.items()))
        keys_by_update = list(inv_d.keys())
        post.save(update_fields=keys_by_update)
        return HttpResponseRedirect ("/posts/")


class Delete_Post (View):
    #Удаляет пост по id
    def get (self,request, post_id, *args,**kwargs):
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect ("/posts/") 
        return JsonResponse ({"Status":"Deleted"})
                

#Для красивого вывода данных:
def parse_posts(post: Post):
    return {'id':post.id, 'title':post.title,'text':post.text, 'counter':post.counter}


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

class PostsView(View):
    #Выводит все посты и считает их количество 
    def get(self,request):
        # all_posts = {
        #     'Posts':[]
        # }
        # posts = Post.objects.all().order_by('id')
        # for post in posts:
        #     all_posts['Posts'].append(parse_posts(post))
        # all_posts['count'] = posts.count()
        # return JsonResponse(all_posts)
        posts = Post.objects.all()
        template = loader.get_template("post_and_comments/all_posts.html")
        context = {
            "posts":posts,
        }

        return HttpResponse(template.render(context,request))


    #Создает (если не создан) пост по введенным данным 
    # (POST - Body - form-data)
    @csrf_exempt
    def post(self,request):
        # id = request.POST.get('id')
        title = request.POST.get('title')
        text = request.POST.get('text')
        counter = request.POST.get('counter')
        category = request.POST.get('category')
        # date_create = request.POST.get('date_create')
        post, is_created = Post.objects.get_or_create(title=title, text=text,counter=counter,category=category)
        return HttpResponseRedirect ("")
        
    
class Transit_Get_Post(View):
    def get (self,request):
        template = loader.get_template("post_and_comments/create_post.html")
        return HttpResponse(template.render(request))

class Transit_Update_Post(View):
    def get (self,request, post_id):
        template = loader.get_template("post_and_comments/update_post.html")
        context = {
            "post_id":post_id,
        }
        return HttpResponse(template.render(context,request))
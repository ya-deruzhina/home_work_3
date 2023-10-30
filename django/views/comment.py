# Здесь будут операции с комментариями: вывод по id, создание, редактирование, удаление
from django.shortcuts import render
from django.http import JsonResponse
from posts.models import Comment, Post
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.db import transaction
from django.template import loader
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest,HttpResponseRedirect


class CommentView(View):
    # Получить комменты у поста по id
    def get (self,request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)
        comments = Post.objects.get(id=post_id).comments.all()
        template = loader.get_template("post_and_comments/view_all_comments.html")
        context = {
            "comments":comments,
        }

        return HttpResponse(template.render(context,request))


    
    #Создаем комментарий с привязкой к посту через post-body-form data
    @csrf_exempt
    def post(self,request, post_id, *args, **kwargs):
        # new_id = request.POST.get('id')
        text = request.POST.get('text')
        status = request.POST.get('status')
        post = Post.objects.get(id=post_id)

        comment = Comment(text=text, new = post,status=status)
        comment.save()

        return JsonResponse ({"Status": "Created"})
        

    #Удаляет пост по id
    def delete(self,request, post_id, *args,**kwargs):
        id_by_comment = Comment.objects.filter(id=post_id)
        if len(id_by_comment) !=0:
            post = Comment.objects.get(id=post_id)
            post.delete() 
            return JsonResponse ({"Status":"Deleted"})
        else:
            return JsonResponse ({"Status":"Not Created"})

class Comment_postView(View):
    @transaction.atomic
    def post (self,request,post_id):
        id_comment = Comment.objects.get(id=post_id)
        id_comment.status = "changed"
        id_comment.save(update_fields=["status"])
        id_post = Post.objects.get(id=post_id)
        id_post.text = "changed"
        id_post.save(update_fields=["text"])    
        return JsonResponse ({"Status":"Ok"})
    
class OneComment (View):    
    #Выводит коммент по id
    def get (self, request, comment_id,  *args,**kwargs):

        comment = Comment.objects.get(id= comment_id)    
        template = loader.get_template("post_and_comments/view_one_comment.html")
        context = {
            "comment":comment,
        }
        return HttpResponse(template.render(context,request))

    
    # @csrf_exempt
    # def get (self,request,post_id):
    #     id_comment = Comment.objects.get(id=post_id)
    #     comment = (Comment(id = id_comment,status="changed")).save()

    #     with transaction.atomic(self):
    #         id_post = Post.objects.get(id=post_id)
    #         post = (Post(id = id_post,text="changed")).save()
    
    #     return JsonResponse ({"Status":"Ok"})

        #Создаем комментарий с привязкой к посту через post-body-form data
    # @csrf_exempt

class Create_Comment (View):
    def post (self,request, post_id, *args, **kwargs):
        new_id = post_id
        text = request.POST.get('text')
        status = request.POST.get('status')
        
        comment = Comment(text=text, new_id = new_id,status=status)
        comment.save()

        return HttpResponseRedirect ("/posts/")
        return JsonResponse ({"Status": "Created"})


class Transit_Get_Comment(View):
    def get (self,request, post_id):
        template = loader.get_template("post_and_comments/create_comment.html")
        context = {
            "post_id":post_id,
        }
        return HttpResponse(template.render(context,request))
    
class Delete_Comment(View):
    #Удаляет пост по id
    def get (self,request, comment_id, *args,**kwargs):
        id_by_comment = Comment.objects.filter(id=comment_id)
        if len(id_by_comment) !=0:
            post = Comment.objects.get(id=comment_id)
            post.delete() 
            return HttpResponseRedirect ("/posts/") 
        else:
            return JsonResponse ({"Status":"Not Created"})
        

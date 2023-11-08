# Здесь будут операции с комментариями: вывод по id, создание, редактирование, удаление
from django.shortcuts import render
from django.http import JsonResponse
from post_form_html.models import CommentForm, PostForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.db import transaction
from django.template import loader
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest,HttpResponseRedirect
from post_form_html.forms.create_comment_form import AddCommentForm
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView



class CommentView(View):
    # Получить комменты у поста по id
    def get (self,request, post_id, *args, **kwargs):
        post = PostForm.objects.get(id=post_id)
        comments = PostForm.objects.get(id=post_id).comments.all()
        template = loader.get_template("post_and_comments/view_all_comments.html")
        context = {
            "comments":comments,
        }

        return HttpResponse(template.render(context,request))


    
    #Создаем комментарий с привязкой к посту через post-body-form data
    @csrf_exempt
    def post(self,request, post_id, *args, **kwargs):
        text = request.POST.get('text')
        status = request.POST.get('status')
        post = PostForm.objects.get(id=post_id)

        comment = CommentForm(text=text, new = post,status=status)
        comment.save()

        return JsonResponse ({"Status": "Created"})
        

    
class OneComment (View):    
    #Выводит коммент по id
    def get (self, request, comment_id,  *args,**kwargs):

        comment = CommentForm.objects.get(id= comment_id)    
        template = loader.get_template("post_and_comments/view_one_comment.html")
        context = {
            "comment":comment,
        }
        return HttpResponse(template.render(context,request))

    
    
class Create_Comment (View):
    def post (self,request, post_id, *args, **kwargs):
        new_id = post_id
        text = request.POST.get('text')
        status = request.POST.get('status')
        
        comment = CommentForm(text=text, new_id = new_id,status=status)
        comment.save()

        return HttpResponseRedirect ("/post_forms_html/")
    

class Transit_Get_Comment(View):
    def get (self,request, post_id):
        template = loader.get_template("post_and_comments/create_comment.html")
        context = {
            "post_id":post_id,
            "form":AddCommentForm()
        }
        return HttpResponse(template.render(context,request))
    
    
class Delete_Comment(View):
    #Удаляет пост по id
    def get (self,request, comment_id, *args,**kwargs):
        id_by_comment = CommentForm.objects.filter(id=comment_id)
        if len(id_by_comment) !=0:
            post = CommentForm.objects.get(id=comment_id)
            post.delete() 
            return HttpResponseRedirect ("/post_forms_html/") 
        else:
            return JsonResponse ({"Status":"Not Created"})
        

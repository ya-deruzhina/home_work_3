from django.shortcuts import render
from django.http import JsonResponse

POSTS = [
    {
        'title': 'first post',
        'text':'post1'
    },
    {
        'title': 'second post',
        'text':'post2'
    },
    {
        'title': 'last post',
        'text':'post3'
    }
]


# Create your views here.
def get_post(request):
    text_post = []

    for post in POSTS:
        text_post.append(post)

    return JsonResponse(text_post,safe=False)

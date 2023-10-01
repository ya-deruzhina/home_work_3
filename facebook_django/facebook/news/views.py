from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_new(request):
    return HttpResponse("Hello, world. We create first view.")

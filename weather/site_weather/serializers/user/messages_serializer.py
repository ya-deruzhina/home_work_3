from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from site_weather.models import SiteUserModel, User, MessagesUserModel
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
import json
import hashlib
from django.contrib.auth.hashers import make_password



class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesUserModel
        fields = ["message","user_page_id","autor_message"]

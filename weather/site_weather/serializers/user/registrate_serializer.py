from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from site_weather.models import SiteUserModel, User
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
import json
import hashlib
from django.contrib.auth.hashers import make_password



# class RegisterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SiteUserModel
#         fields = ["name","password","user_zodiac"]

#     def create(self, validated_data):
#         # user = SiteUserModel(validated_data)
#         return SiteUserModel.objects.create(**validated_data)
       
#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","user_zodiac"]

    def create(self, validated_data):
        return User.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
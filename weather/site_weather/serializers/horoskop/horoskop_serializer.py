from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from site_weather.models import HoroskopModel
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
import json
from django.contrib.auth.models import User


class HoroskopSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoroskopModel
        fields = ["zodiac","description"]

    def create(self, validated_data):
        return HoroskopModel.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

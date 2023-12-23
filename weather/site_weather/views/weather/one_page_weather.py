from site_weather.models import Weather
from django.http import HttpResponse 
from django.views import View
from django.template import loader
from site_weather.serializers import WeatherCommonSerializer 
from rest_framework import generics


# Выводит Json
class OneWeatherView(generics.RetrieveAPIView):
    weather_id = 1
    queryset = Weather.objects.all()
    serializer_class = WeatherCommonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'weather_id'
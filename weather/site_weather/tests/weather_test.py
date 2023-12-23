# Create your tests here.

from django.test import TestCase,Client
from rest_framework.test import APIRequestFactory, APITestCase
from site_weather import models
import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
import requests




# Тест на вывод информации (get)
# Внимание!!! Перед началом теста проверить даты в setUp и поставить city="all" в weather.py (view)
class ListWeatherTestCase(APITestCase):
    def setUp(self):
        self.weathers = []
        weather = models.Weather(
            id = 1,
            city = 'Minsk',
            date = "2023-11-30",
            temperature = 15,
            pressure = 10,
            wind = 15.3,
            weather = 'SUN',
        )
        weather.save()
        self.weathers.append(weather)


        weather = models.Weather(
            id = 2,
            city = 'Minsk',
            date = "2023-12-01",
            temperature = 15,
            pressure = 10,
            wind = 15.3,
            weather = 'RAIN',
        )
        weather.save()
        self.weathers.append(weather)
        
        weather = models.Weather(
            id = 3,
            city = 'Minsk',
            date = "2023-12-02",
            temperature = 15,
            pressure = 10,
            wind = 15.3,
            weather = 'SUN',
        )
        weather.save()
        self.weathers.append(weather)

        weather = models.Weather(
            id = 4,
            city = 'Minsk',
            date = "2023-12-03",
            temperature = 15,
            pressure = 10,
            wind = 15.3,
            weather = 'FOGGY',
        )
        weather.save()
        self.weathers.append(weather)

        weather = models.Weather(
            id = 5,
            city = 'Minsk',
            date = "2023-12-04",
            temperature = 15,
            pressure = 10,
            wind = 15.3,
            weather = 'RAIN',
        )
        weather.save()
        self.weathers.append(weather)

        weather = models.Weather(
            id = 6,
            city = 'Minsk',
            date = "2023-12-05",
            temperature = 15,
            pressure = 10,
            wind = 15.3,
            weather = 'SUN',
        )
        weather.save()
        self.weathers.append(weather)

        weather = models.Weather(
            id = 7,
            city = 'Minsk',
            date = "2023-12-06",
            temperature = 15,
            pressure = 10,
            wind = 15.3,
            weather = 'RAIN',
        )
        weather.save()
        self.weathers.append(weather)
        self.id_weathers = {weather.id:weather for weather in self.weathers}
        # import pdb; pdb.set_trace()
        self.city = 'Minsk'


    def test_weathers_list(self):
        # Чтобы это отрабатывало, надо добавлять name = 'ulr_name' в urls.py
        url = reverse('weather-base')
        response = self.client.get(url)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['weather']), len(self.weathers))

        for item in response.data['weather']:
            # import pdb; pdb.set_trace()
            weather = self.id_weathers[item['id']]
            self.assertEqual(item['city'], weather.city)
            self.assertEqual(item['temperature'], weather.temperature)            
            self.assertEqual(item['date'], weather.date)
            self.assertEqual(item['pressure'], weather.pressure)
            self.assertEqual(item['wind'], weather.wind)
            self.assertEqual(item['weather'], weather.weather)

    def test_one_weather(self):
        # Для проверки мы меняем данные weather_id и self.weathers[0]
        # Чтобы это отрабатывало, надо добавлять name = 'ulr_name' в urls.py
        url = reverse('weather-one', kwargs = {'weather_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()

        item = response.data
        self.assertEqual(item['temperature'], self.weathers[0].temperature)
        self.assertEqual(item['date'], self.weathers[0].date)
        self.assertEqual(item['pressure'], self.weathers[0].pressure)
        self.assertEqual(item['wind'], self.weathers[0].wind)
        self.assertEqual(item['weather'], self.weathers[0].weather)

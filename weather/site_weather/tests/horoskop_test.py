from django.test import TestCase,Client
from rest_framework.test import APIRequestFactory, APITestCase
from site_weather import models
import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

# Тест на вывод информации (get)
class TestHoroskop (APITestCase):
    def setUp(self):
        self.horoskops =[]
        horoskop = models.HoroskopModel(
        zodiac = "ARIES",
        description = "New Description",
        date_create_zodiac = "2023-12-03 00:00:00.000 +0300",
        )
        horoskop.save()
        self.horoskops.append(horoskop)
          
        horoskop = models.HoroskopModel(
        zodiac = "TAURUS",
        description = "New Description",
        date_create_zodiac = "2023-12-03 00:00:00.000 +0300",
        )
        horoskop.save()
        self.horoskops.append(horoskop)
            
        self.some_horoskops = {horoskop.zodiac:horoskop for horoskop in self.horoskops}


    def test_all_list(self):
        # Чтобы это отрабатывало, надо добавлять name = 'ulr_name' в urls.py
        url = reverse('horoskop-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['horoskop']), len(self.horoskops))

        for item in response.data['horoskop']:
            horoskop = self.some_horoskops[item['zodiac']]
            self.assertEqual(item['description'], horoskop.description)
            # import pdb; pdb.set_trace()
            # Дату не вывожу, потому что в сериалайзере она не обрабатывается

    def test_one_horoskop(self):
        # Для проверки мы меняем данные weather_id и self.weathers[0]
        # Чтобы это отрабатывало, надо добавлять name = 'ulr_name' в urls.py
        url = reverse('horoskop-one', kwargs = {'zodiac':"ARIES" })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()

        item = response.data
        self.assertEqual(item['description'], self.horoskops[0].description)

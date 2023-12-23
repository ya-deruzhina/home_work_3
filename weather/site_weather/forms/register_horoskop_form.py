from django.forms import ModelForm
from site_weather.models import SiteUserModel, User 
from django import forms

# class RegisterHoroskopForm (ModelForm):
#     class Meta:
#         model = SiteUserModel
#         fields = ["name","password","user_zodiac"]

class RegisterHoroskopForm (ModelForm):
    class Meta:
        model = User
        fields = ["username","password","user_zodiac"]
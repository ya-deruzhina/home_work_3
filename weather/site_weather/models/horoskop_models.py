from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HoroskopModel (models.Model):
    ARIES = "ARIES"
    TAURUS = "TAURUS"
    GEMINI = "GEMINI"
    CANCER = "CANCER"
    LEO = "LEO"
    VIRGO = "VIRGO"
    LIBRA = "LIBRA"
    SCORPIO = "SCORPIO"
    SAGITTARIUS = "SAGITTARIUS"
    CAPRICORN = "CAPRICORN"
    AQUARIUS = "AQUARIUS"
    PISCES = "PISCES"

    KIND_ZODIACS = [
        (ARIES, "Aries"),
        (TAURUS, "Taurus"),
        (GEMINI, "Gemini"),
        (CANCER, "Cancer"),
        (LEO, "Leo"),
        (VIRGO, "Virgo"),
        (LIBRA, "Libra"),
        (SCORPIO, "Scorpio"),
        (SAGITTARIUS, "Sagittarius"),
        (CAPRICORN, "Capricorn"),
        (AQUARIUS, "Aquarius"),
        (PISCES, "Pisces"),

    ]

# Aries -  21.03–20.04
# Taurus - 21.04–21.05
# Gemini - 22.05–21.06
# Cancer - 22.06–22.07
# Leo - 23.07–21.08
# Virgo - 22.08–23.09
# Libra - 24.09–23.10
# Scorpio - 24.10–22.11
# Sagittarius - 23.11–22.12
# Capricorn - 23.12–20.01
# Aquarius - 21.01–19.02
# Pisces - 20.02–20.03


    zodiac = models.CharField (choices=KIND_ZODIACS,primary_key=True)
    description = models.CharField()
    date_create_zodiac = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.zodiac



# Пересмотреть, возможно у джанго есть привязка к админке
class SiteUserModel (models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=30)
    date_create = models.DateTimeField(auto_now_add = True)
    user_zodiac = models.ForeignKey(HoroskopModel, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
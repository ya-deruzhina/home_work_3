from site_weather.models import HoroskopModel,User
from site_weather.serializers import HoroskopSerializer
from site_weather.forms import CreateHoroskopForm,UpdateHoroskopForm

from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.views import View
from django.template import loader

from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

class HoroskopBaseAfterAuthView(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        user_id = request.auth['user_id']
        # ToDo - придумать, как это брать одним запросом. Возможно через сериалайзер
        zodiac_user = User.objects.get(id=user_id).user_zodiac
        username = User.objects.get(id=user_id).username
        horoskop = HoroskopModel.objects.filter(zodiac=zodiac_user)
        if len(horoskop)==0:
            return JsonResponse ({"Status": "Horoskop Not Created"})
        else:
            horoskop = horoskop[0]
            template = loader.get_template("horoskop/base_after_auth_page.html")
            context = {
                "horoskop":horoskop,
                "username":username
            }
            return HttpResponse(template.render(context,request))
from site_weather.models import HoroskopModel
from site_weather.serializers import HoroskopSerializer
from site_weather.forms import CreateHoroskopForm,UpdateHoroskopForm

from django.http import HttpResponse,HttpResponseRedirect 
from django.views import View
from django.template import loader

from rest_framework import generics
from rest_framework.views import APIView

# Страничка гороскопа
class HoroskopOne (generics.RetrieveAPIView):
    queryset = HoroskopModel.objects.all()
    serializer_class = HoroskopSerializer
    lookup_field = 'zodiac'
    lookup_url_kwarg = 'zodiac'

# Создать новый гороскоп (добавить проверку Foreign Key)
class HoroskopCreateTransit(APIView):
    def get (self, request):
        template = loader.get_template("horoskop/create_horoskop.html")
        context = {
            "form":CreateHoroskopForm()
        }
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        # import pdb; pdb.set_trace()
        serializer = HoroskopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponseRedirect ("/weather/horoskop/all/")

# Обновление description гороскопа
# Работает через Постмэн и запрос Patch (цепочка настроена, но из-за неправильного запроса обрывается)    
class HoroskopUpdate(generics.UpdateAPIView):
    queryset = HoroskopModel.objects.all()    
    serializer_class = HoroskopSerializer
    lookup_field = 'zodiac'
    lookup_url_kwarg = 'zodiac'

# Транзит для Update
class HoroskopUpdateTransit(View):
    def get (self,request,zodiac):
        horoskop = HoroskopModel.objects.get(zodiac=zodiac)
        template = loader.get_template("horoskop/horoskop_update.html")
        context = {
            "horoskop":horoskop,
            "form":UpdateHoroskopForm()
        }
        return HttpResponse(template.render(context,request))
    

# Удаление одной карточки - через Постмэн
class OneHoroskopDelete (generics.DestroyAPIView):
    queryset = HoroskopModel.objects.all()    
    serializer_class = HoroskopSerializer
    lookup_field = 'zodiac'
    lookup_url_kwarg = 'zodiac'
from site_weather.models import HoroskopModel,MessagesUserModel,User
from site_weather.serializers import HoroskopSerializer, MessagesSerializer
from site_weather.forms import CreateHoroskopForm,UpdateHoroskopForm,CreateMessageForm

from django.http import HttpResponse,HttpResponseRedirect, JsonResponse 
from django.views import View
from django.template import loader

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Посмотреть все (рядом удалить)
# Написать новое
class MessageView(APIView):
    # Страница со всеми сообщения + оставить новое
    def get(self,request):
        permission_classes = [IsAuthenticated]
        id_user = request.auth['user_id']
        username = User.objects.get(id=id_user).username

        # id_user = User.objects.get(username=username).id
        message = MessagesUserModel.objects.filter(user_page_id=id_user).order_by('date_create')
        template = loader.get_template("message/messages_main.html")
        context = {
            "messages":message,
            "form":CreateMessageForm(),
            "username":username
        }
        return HttpResponse(template.render(context,request))
   
    def post(self,request):
        permission_classes = [IsAuthenticated]
        id_user = request.auth['user_id']
        username = User.objects.get(id=id_user).username
        message = request.POST.get('message')
        autor_message=request.POST.get('autor_message',username)
        messages = MessagesUserModel(message=message, user_page_id = id_user,autor_message=autor_message)
        messages.save()
        return HttpResponseRedirect ("")

class MessageViewHTML(APIView):
    # Страница со всеми сообщения + оставить новое
    def get(self,request,username):
        id_user = User.objects.get(username=username).id
        message = MessagesUserModel.objects.filter(user_page_id=id_user).order_by('date_create')
        template = loader.get_template("message/messages_main_html.html")
        context = {
            "messages":message,
            "form":CreateMessageForm(),
            "username":username
        }
        return HttpResponse(template.render(context,request))
   
    def post(self,request,username):
        id_user = User.objects.get(username=username).id
        message = request.POST.get('message')
        autor_message=request.POST.get('autor_message',username)
        messages = MessagesUserModel(message=message, user_page_id = id_user,autor_message=autor_message)
        messages.save()
        return HttpResponseRedirect ("")
    


# Удаление одной карточки - через Постмэн
class MessageDelite (generics.DestroyAPIView):
    queryset = MessagesUserModel.objects.all()    
    serializer_class = MessagesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest
from posts.models import Wallet
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.template import loader

class WalletsView(View):
    def post (self,request, *args, **kwargs):
        name = request.POST.get('name','')
        currency = request.POST.get('currency','')        
        
#        name = json.loads(request.body.decode('utf-8').get('name'))
#        currency = json.loads(request.body.decode('utf-8').get('currency'))

        if not name or not currency:
            return HttpResponseBadRequest('Name or Currensy is empty')

        wallet = Wallet(name=name, currency=currency)
        wallet.save()
        return JsonResponse(data=wallet.serilize_from_db())


    def get (self,request, *args, **kwargs):
        wallets = Wallet.objects.all()
        template = loader.get_template("wallets/wallets_list.html")
        context = {
            "wallets":wallets,
        }

        return HttpResponse(template.render(context,request))
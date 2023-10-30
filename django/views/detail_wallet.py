from django.shortcuts import render
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest
from posts.models import Wallet
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import get_object_or_404
from django.template import loader

class DetailWallet(View):
    def get (self,request, _id, *args, **kwargs):
        wallet = get_object_or_404(Wallet, id=_id)
        template = loader.get_template("wallets/wallet_details.html")
        context = {
            "wallet":wallet
        }

        return HttpResponse(template.render(context,request))
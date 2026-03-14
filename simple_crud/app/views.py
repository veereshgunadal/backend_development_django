from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import json
# Create your views here.

def get(request):
    response = json.dumps({'method':'get', 'code':200, 'message':'i am get api'})
    return JsonResponse({'method':'get', 'code':200, 'message':'i am get api'})
    #return HttpResponse(response)

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods

import json
# Create your views here.

def get(request):
    response = json.dumps({'method':'get', 'code':200, 'message':'i am get api'})
    return JsonResponse({'method':'get', 'code':200, 'message':'i am get api'})
    #return HttpResponse(response)

#@require_POST
@require_http_methods(['POST'])
def post(request):
    response = json.dumps({'method':'post', 'code':200, 'message':'i am post api'})
    return JsonResponse({'method':'post', 'code':200, 'message':'i am post api'})
    #return HttpResponse(response)

@require_http_methods(['DELETE'])
def delete(request):
    response = json.dumps({'method':'delete', 'code':200, 'message':'i am delete api'})
    return JsonResponse({'method':'delete', 'code':200, 'message':'i am delete api'})
    #return HttpResponse(response)

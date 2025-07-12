from django.http import JsonResponse, HttpResponse, HttpRequest
import json


def request(request: HttpRequest):
    response = JsonResponse({})
    
    print(request.GET)
    print(json.loads(request.body))
    
    if request.method == "GET":
        obj = { "data": 5 }
        response = JsonResponse(obj)
    else:
        response = HttpResponse("Request method must be GET")
        
    return response
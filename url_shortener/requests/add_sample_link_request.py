from django.http import JsonResponse, HttpResponse, HttpRequest
import json

from url_shortener.models.URL import URL


def request(request: HttpRequest):
    response = JsonResponse({})
    
    if request.method == "GET":
        new_url = URL(origin_url="sample_origin_url", shortened_code="sample_shorter_url")
        new_url.save()
        obj = { "data": 5 }
        response = JsonResponse(obj)
    else:
        response = HttpResponse("Request method must be GET")
        
    return response

from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse, HttpResponse, HttpRequest
import json

from url_shortener.models.URL import URL

import uuid


def make_new_record(request: HttpRequest):
    response = JsonResponse({})
    
    if request.method == "GET":
        request_body = json.loads(request.body)
        
        is_unique = request_body['unique']
        url = request_body['url']
        code = ""
        
        if is_unique or len(URL.objects.filter(origin_url=url)) == 0:
            code = uuid.uuid4().hex
            while len(URL.objects.filter(shortened_code=code)) > 0:
                code = uuid.uuid4().hex
            
            URL(
                origin_url=request_body['url'],
                shortened_code=code
            ).save()
        else:
            code = URL.objects.filter(origin_url=url)[0].shortened_code
        
        obj = {
            "code": code
        }
        
        response = JsonResponse(obj)
    else:
        response = HttpResponse("Request method must be GET")
        
    return response


def get_summary(request: HttpRequest):
    response = JsonResponse({})
    
    if request.method == "GET":
        request_body = json.loads(request.body)
        
        code = request_body['code']
        if len(URL.objects.filter(shortened_code=code)) > 0:
            url = URL.objects.filter(shortened_code=code)[0]
            response = JsonResponse({
                "ok": True,
                "origin_url": url.origin_url, 
                "shortened_code": url.shortened_code,
                "full_url": request.build_absolute_uri(f'r/{url.shortened_code}'),
                "times_used": url.times_used,
                "unique": "" # TODO
            })
        else:
            response = JsonResponse({
                "ok": False,
                "error": "No entry registered with the given code"
            })
    else:
        response = HttpResponse("Request method must be GET")
        
    return response

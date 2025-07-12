from django.shortcuts import redirect
from django.http import JsonResponse, HttpRequest, HttpResponse
from url_shortener.models.URL import URL


def request(request: HttpRequest, code):
    response = JsonResponse({})
    
    if request.method == "GET":
        urls = URL.objects.filter(shortened_code=code)
        
        if len(urls) > 0:
            url = urls[0].origin_url
            urls[0].times_used += 1
            urls[0].save()
            response = redirect(url)
        else:
            response = JsonResponse({})
        
    else:
        response = HttpResponse("Request method must be GET")
        
    return response
    
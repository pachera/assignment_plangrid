from django.shortcuts import render
from django.http import JsonResponse

import logging

logger = logging.getLogger(__name__)

# Create your views here.

def hello_world(request):

    #logger.debug(request.META['HTTP_HOST'] + request.META['QUERY_STRING'])
    logger.debug(request.build_absolute_uri())

    if request.META['HTTP_ACCEPT'] == 'application/json':
    	return JsonResponse({'message': "Hello, World!"})
    else:
        return render(request, 'mytest/hello_world.html', {})

def hello_world_html(request):

    return render(request, 'mytest/hello_world.html', {})

def hello_world_json(request):

    return JsonResponse({'message': "Hello, World!"})

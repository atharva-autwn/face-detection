from django.shortcuts import render
from .detection import *
from .recognize_faces_image import *
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.decorators import api_view
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def default(request):
    return render(request, 'recognise/video.html')

def recognise_view(request):
    name = recognize(start())
    return HttpResponse('<h1>' + str(name[0]) + '</h1>')
'''
@csrf_exempt
def image(request, format=None):
    if request.method == 'POST':
        image = np.array(JSONParser().parse(request)['image'])
        name = recognize(image)
        print(name)
        data = {'name': name}
        return JsonResponse(data, status=201)
        #return HttpResponse('<h1>' + str(name[0]) + '</h1>')
'''
class image(APIView):
    def post(self, request,format=None):
        #print(request.POST)
        #print(type(request))
        data = request.data
        #print(data)
        #print(type(data.values()))
        image = np.array(data['image'])
        print(type(image))
        name = recognize(image)
        #print(name)
        data = {'name':name[0]}
        return Response(data,status=status.HTTP_201_CREATED)
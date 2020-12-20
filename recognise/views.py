from django.shortcuts import render
from .detection import *
from .recognize_faces_image import *
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.decorators import api_view
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import cv2

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
    #parser_classes = (MultiPartParser, FormParser)
    def post(self, request,format=None):
        #print(request.POST)
        #print(type(request))
        data = request.data
        #print(data)
        #print(type(data.values()))
        image = np.array(data['image'])
        print(image)
        print(type(image))
        print(image.shape )
        name = recognize(image)
        #print(name)
        data = {'name':name[0]}
        return Response(data,status=status.HTTP_201_CREATED)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import random
import string
from .models import *
from django.http import JsonResponse

@csrf_exempt
def index(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data[0:len(data)])
        #name = 'default'
        temp = len('data:image/jpeg;base64,')
        for d in data:
            d = d[temp:len(d)]
            imgdata = base64.b64decode(d)
            filename = randomString()+'.jpg'  # I assume you have a way of picking unique filenames
            with open('media/'+filename, 'wb') as f:
                f.write(imgdata)
            
            image = cv2.imread('media/'+filename)
            name = recognize(image)
            if name!=[]:
                i = Images.objects.create(name=name[0], file=filename)
            else:
                 i = Images.objects.create(name='unknown', file=filename)
            i.save()
            #print(name)
            #print(image)
        print('Success')
        return HttpResponse('<h1> Success </h1>')
    return render(request, 'recognise/index.html')

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
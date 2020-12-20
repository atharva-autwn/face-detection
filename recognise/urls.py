from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', default , name = 'default'),
    path('recognise/', recognise_view , name = 'recognise'),
    path('image/',image.as_view() ,name='image')
]

urlpatterns = format_suffix_patterns(urlpatterns)
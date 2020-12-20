from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static

urlpatterns = [
    path('', default , name = 'default'),
    path('recognise/', recognise_view , name = 'recognise'),
    path('image/',image.as_view() ,name='image'),
     path('index', index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)
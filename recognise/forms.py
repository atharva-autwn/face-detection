from django import forms
from django.contrib.auth.models import User
from .models import *

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['name','file']
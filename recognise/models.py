from django.db import models
from picklefield.fields import PickledObjectField

class SomeObject(models.Model):
    args = PickledObjectField()

from django.db import models

class Images(models.Model):
    name = models.CharField(max_length=50, )
    file = models.ImageField()

    def __str__(self):
        return self.name

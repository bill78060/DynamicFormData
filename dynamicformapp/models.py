from django.db import models

# Create your models here.

from django.db import models

# dynamicformapp/models.py
from django.db import models

class DynamicFormData(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    data = models.CharField(max_length=255)

    def __str__(self):
        return self.name



    


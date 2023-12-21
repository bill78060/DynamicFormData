from django.contrib import admin

# Register your models here.
# dynamicformapp/admin.py
from django.contrib import admin
from .models import DynamicFormData

admin.site.register(DynamicFormData)

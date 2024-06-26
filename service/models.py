from django.db import models
from django.contrib import admin
from service.models import Service
class ServiceAdmin(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    # service_des=models.TextField()
# Create your models here.
admin.site.register(Service , ServiceAdmin)


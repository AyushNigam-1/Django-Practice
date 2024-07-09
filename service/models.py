from django.db import models
class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    icon = models.FileField(upload_to=",media/",max_length=250 ,null=True , default=None)
    
class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.car_name



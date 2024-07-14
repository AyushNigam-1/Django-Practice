from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class carManager(models.Manager):
    def get_queryset(self):
         return super().get_queryset().filter(is_deleted = False)

class Service(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True)
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    icon = models.FileField(upload_to="media/",max_length=250 ,null=True , default=None)
    
class CustomUser(AbstractBaseUser):
        username = None
        phone_number = models.CharField(max_length=100,unique=True)
        email = models.EmailField(unique=True)
        user_bio = models.CharField(max_length=50)
        user_profile_image = models.ImageField(upload_to='profile')
        
        USERNAME_FIELD = 'phone_numer'
        REQUIRED_FIELDS = []
        objects = UserManager()
    
    
class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.car_name
    
    class Meta:
        # ordering = ['car']
        verbose_name = 'car'
    
    objects = carManager()
    admin_objects = models.Manager()
 


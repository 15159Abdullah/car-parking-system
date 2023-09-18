from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True,default=True)
    is_admin = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    forget_password_token = models.CharField(max_length=1000,blank=True,null=True)
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    
   
    
   

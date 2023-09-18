from django.db import models
from accountss.models import CustomUser

#_____________________AREA_________________________________

class Area(models.Model):
    country = models.CharField(max_length=100 , default=True)
    area_name = models.CharField(max_length=100 , default=True)
 
#_____________________Parking_________________________________

class Parking(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200 , default=True)
    address = models.CharField(max_length=300 , default=True)

#_____________________Slots_________________________________

class Slots(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE,null=True)
    slots_price =  models.IntegerField(default=True)
    slots_number = models.IntegerField(default=True)
    slot_color = models.BooleanField(default=True)

#_____________________Slots Request_________________________________

class Slots_Request(models.Model):
    slots = models.ForeignKey(Slots, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    catogry = models.CharField(max_length=100 , default=True)
    model = models.CharField(max_length=100 , default=True)
    num_plate = models.CharField(max_length=200,default=True)
    phone = models.IntegerField(default=True)
    in_date = models.DateField()
    out_date = models.DateField()
    address = models.CharField(max_length=500 , default=True)
    slot_status = models.BooleanField(default=True)
    payment = models.ImageField(upload_to='public', null=True,blank=True)

class Contact(models.Model):
    name=models.CharField(max_length=50,default=True)
    email =  models.EmailField(default=True)
    subject = models.CharField(max_length=300,default=True)
    message = models.CharField(max_length=500, default=True)

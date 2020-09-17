from django.db import models

# Create your models here.
# class Contact(models.Model):
#     name = models.CharField(max_length=200,blank=False)
#     last_name = models.CharField(max_length=200,blank=False)
#     mobile_number = models.CharField(max_length=100,blank=True)
#     email_id = models.EmailField(blank=False)
#     Blood_type = models.CharField(max_length=100)
#     City = models.CharField(max_length=100)
#     Sample_text = models.CharField(max_length=100)
#     date_day = models.DateField()
#     otp = models.CharField(max_length=6,blank=True)

class Contact1(models.Model):
    name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    mobile_number = models.CharField(max_length=12,blank=True)
    email_id = models.EmailField(blank=False)
    Blood_type = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Sample_text = models.CharField(max_length=100)
    date_day = models.DateField()
    otp = models.CharField(max_length=6, blank=True)
    gender = models.CharField(max_length=10,blank=False)
    is_verified = models.BooleanField(blank=True,default=False)

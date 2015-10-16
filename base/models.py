from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_date

# Create your models here.
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey 


class Customer(models.Model):
       cust_num = models.CharField(max_length=8, unique=True)
       title = models.CharField(max_length=30, blank=False)
       sales = models.ForeignKey(User)
       is_active = models.BooleanField(default=True) 
       create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
       update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

       def __str__(self):
              return self.cust_num + ' ' + self.title 



class Effective(models.Model):

       customer = models.ForeignKey(Customer)
       effective_month = models.IntegerField( default=14 )
       effective_mode = models.IntegerField( default=9 )
       start_date = models.DateField( default= timezone.now )
       end_date = models.DateField( default=parse_date('2050-12-31'))
       is_valid = models.BooleanField(default=True)
       create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
       update_at = models.DateTimeField(auto_now_add=False, auto_now=True)



#Choices Example 
class Person(models.Model):
       SHIRT_SIZES = (
              ('S', 'Small'),
              ('M', 'Medium'),
              ('L', 'Large'),
              )
       name = models.CharField(max_length=60)
       shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Catcode(models.Model):

       scode = models.CharField(max_length=4, blank=False, null=False) #System
       tcode = models.CharField(max_length=4, blank=True, null=True) #Type
       icode = models.CharField(max_length=4, blank=True, null=True)  
       describtion = models.CharField(max_length=60, blank=False, null=False)
       describtion2 = models.CharField(max_length=60, blank=True, null=True)  
       is_embedded = models.BooleanField(default=True) 
       create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
       update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

       class Meta:
              unique_together = ("scode", "tcode", "icode" ,)


       def __str__(self):
              return self.describtion




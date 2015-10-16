from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.dateparse import parse_date
from smart_selects.db_fields import ChainedForeignKey 


class Customer(models.Model):
	cust_num = models.CharField(max_length=8, unique=True)
	title = models.CharField(max_length=30, blank=False)
	sales = models.ForeignKey(User)
	is_active = models.BooleanField(default=True) 

	def __str__(self):
		return self.cust_num + ' ' + self.title 



class Effective(models.Model):
       customer = models.ForeignKey(Customer)
       effective_month = models.IntegerField( default=14 )
       effective_mode = models.IntegerField( default=9 )
       start_date = models.DateField( default=timezone.now())
       end_date = models.DateField( default=parse_date('2050-12-31'))
       is_valid = models.BooleanField(default=True)
       create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
       update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

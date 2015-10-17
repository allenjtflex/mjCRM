from django.db import models

# Create your models here.
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey 
from base.models import Customer, Catcode



class Rejection(models.Model):
	customer = models.ForeignKey(Customer)
	deliver = models.CharField(max_length=30, blank=False )
	deliver_num = models.CharField(max_length=30 )
	cctno = models.CharField(max_length=10 , blank=True, null=True)
	quantity = models.IntegerField(default=1)
	uom = models.ForeignKey(Catcode)
	wmemo = models.TextField(blank=True, null=True)
	smemo = models.TextField(blank=True, null=True)
	deliver_at = models.DateField( default= timezone.now)
	create_at = models.DateTimeField(auto_now_add=True, auto_now = False)
	update_at = models.DateTimeField(auto_now_add=False, auto_now = True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.deliver

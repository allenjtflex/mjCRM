from django.db import models

# Create your models here.
class Barcode(models.Model):
	bformat = models.CharField(max_length=4, blank=False, null=False)
	barcodelen = models.IntegerField()
	regexpstring = models.CharField(max_length=254, blank=False, null=False)

	def __str__(self):
		return self.bformat
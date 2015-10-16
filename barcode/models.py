from django.db import models

# Create your models here.
class Barcode(models.Model):
	bformat = models.CharField(max_length=4, blank=False, null=False)
	barcodelen = models.IntegerField()
	regexpstring = models.CharField(max_length=254, blank=False, null=False)

	class Meta:
		ordering = ['bformat']


	def __str__(self):
		return self.bformat



class Definecaption(models.Model):
	caption = models.CharField(max_length=100, blank=False, null=False)

	class Meta:
		ordering = ['id']


	def __str__(self):
		return self.caption



class Encoder(models.Model):
	bformat = models.ForeignKey(Barcode)
	caption = models.ForeignKey(Definecaption)	
	start_position = models.IntegerField()
	char_length = models.IntegerField()

	class Meta:
		ordering = ['bformat', 'start_position']
		

	def __str__(self):
		return str(self.start_position)


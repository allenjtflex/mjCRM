from django.shortcuts import render
# Create your views here.
from barcode.models import Barcode
from barcode.forms import testForm
import re

def barcodetest(request):
	form = testForm(request.POST or None)
	if form.is_valid():
		barcode = form.cleaned_data.get('barcode')
		ibarcode = barcode
		print('Input Barcode is: %s'%barcode)
		print('Input Length is: %s'%len(barcode))

		barcodes = Barcode.objects.filter(barcodelen= len(barcode)).values()
		#print(type(barcodes))
		print('Query_set Length : %s'%barcodes.count())
		if barcodes.count()>0:
			for barcode in barcodes:
				for key, value in barcode.items():
					if key=='regexpstring':
						regstr = value
						print( regstr )
						result = re.match(str(regstr), ibarcode, 'True')
						print( result )
						
		#print('Input Format Have : %s'%barcodes[0].bformat)

	"""
	
	barcodes = Barcode.objects.filter(barcodelen= length)
	
	"""

	return render(request, 'barcodetest.html', locals())

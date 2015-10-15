from django.shortcuts import render
# Create your views here.
from barcode.models import Barcode
from barcode.forms import testForm

def barcodetest(request):
	form = testForm(request.REQUEST or None)
	if form.is_valid():
		barcode = form.cleaned_data.get('barcode')
		print('Input Barcode is: %s'%barcode)
		print('Input Length is: %s'%len(barcode))

		barcodes = Barcode.objects.filter(barcodelen= len(barcode)).values()
		print(type(barcodes))
		print('Query_set Length : %s'%barcodes.count())
		#print('Input Format Have : %s'%barcodes[0].bformat)

	"""
	
	barcodes = Barcode.objects.filter(barcodelen= length)
	
	"""

	return render(request, 'barcodetest.html', locals())

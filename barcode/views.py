from django.shortcuts import render
# Create your views here.
from barcode.models import Barcode
from barcode.forms import testForm
import re

def barcodetest(request):
	form = testForm(request.POST or None)
	if form.is_valid():
		barcode = form.cleaned_data.get('barcode').strip()
		barcodelength = len(barcode)

		print('Input Barcode is: %s'%barcode)
		print('Input Length is: %s'%len(barcode))

		barcodes = Barcode.objects.filter(barcodelen= barcodelength)
		
		#print(barcodes.count())
		if barcodes.count()>0:
			for barformat in barcodes:
				result = re.match( barformat.regexpstring , barcode)
				if result:
					#print(barformat.regexpstring)
					matchsformats = Barcode.objects.get(regexpstring= barformat.regexpstring)
					#print(matchsformats)

	return render(request, 'barcodetest.html', locals())

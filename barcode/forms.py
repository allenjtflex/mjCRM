from django import forms


class testForm(forms.Form):
	barcode = forms.CharField(max_length=128)

from django import forms
from django.utils import timezone


from .models import Rejection
from base.models import Customer, Catcode


class DeliverForm(forms.Form):
	deliver_at = forms.DateField()
	customer = forms.CharField()
	deliver = forms.CharField()
	deliver_num = forms.CharField()
	cctno = forms.CharField()
	quantity = forms.IntegerField()	





class RejectionForm(forms.ModelForm):
	uom = forms.ModelChoiceField(queryset= Catcode.objects.filter(scode='SYS1', tcode='UOM').exclude(icode=''), initial =0)

	class Meta:
		model = Rejection
		#fields = ['deliver_at','customer','deliver','deliver_num','cctno','quantity','wmemo','smemo']
		exclude = ['create_at','update_at', 'smemo',]
		







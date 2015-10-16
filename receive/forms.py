from django import forms
from django.utils import timezone


from .models import Rejection
from base.models import Customer, CatCode


class DeliverForm(forms.Form):
	deliver_at = forms.DateField()
	customer = forms.CharField()
	deliver = forms.CharField()
	deliver_num = forms.CharField()
	cctno = forms.CharField()
	quantity = forms.IntegerField()	





class RejectionForm(forms.ModelForm):
	class Meta:
		model = Rejection
		exclude = ['create_at']







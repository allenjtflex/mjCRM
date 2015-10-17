from django.shortcuts import render

from django.http import HttpResponseRedirect

from .forms import RejectionForm, DeliverForm
from .models import Rejection
# Create your views here.


def rejectionlist(request):
	title='Rejection Lists'
	rejections = Rejection.objects.all()
	return render(request, 'rejectionlist.html', locals())

def rejectionform(request):
	title='New Rejection'
	form = RejectionForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/rejectionlist')


	return render(request, 'rejection.html', locals())

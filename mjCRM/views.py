from django.shortcuts import render



def home(request):
	title = "MyCRM Home"
	return render(request, 'index.html', locals())
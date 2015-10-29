from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def home_page(request):
	return render(request, 'home.html')
#	return HttpResponse('<html><title>To-Do list<title><h1>Umroh Machfudza Sihaloho\'s To-Do List</h1></html>')	


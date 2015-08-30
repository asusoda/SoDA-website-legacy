from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context_dict = {}
	context_dict['current_page'] = "Welcome to SoDA!"
	return render(request,'index.html',context_dict)


def calendar(request):
	
	context_dict = {}
	context_dict['current_page'] = 'Calendar'
	
	return render(request,'calendar.html',context_dict)

def aboutus(request):
	
	context_dict = {}
	context_dict['current_page'] = "About Us"
	
	return render(request,'about-us.html',context_dict)

def sponsors(request):
	
	context_dict = {}
	context_dict['current_page'] = 'Sponsors'
	return render(request,'sponsors.html',context_dict)

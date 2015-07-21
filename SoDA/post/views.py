from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request,'index.html')
def announcements(request):
	return render(request,'announcements.html')
def competitions(request):
	return render(request,'competitions.html')
def calendar(request):
	return render(request,'calendar.html')
def aboutus(request):
	return render(request,'about-us.html')
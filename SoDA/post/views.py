from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request,'post/index.html')
def announcements(request):
	return render(request,'post/announcements.html')
def competitions(request):
	return render(request,'post/competitions.html')
def calendar(request):
	return render(request,'post/calendar.html')
def aboutus(request):
	return render(request,'post/about-us.html')
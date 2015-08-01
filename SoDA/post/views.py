from django.shortcuts import render
from django.http import HttpResponse
from post.models import Announcement, Competition

# Create your views here.
def index(request):
	context_dict = {}
	context_dict['current_page'] = "Welcome to SoDA!"
	return render(request,'post/index.html',context_dict)

def announcements(request):
	#Holds the queries to be dislayed on the front end
	context_dict = {}
	context_dict['current_page'] = "Newsletter"
	context_dict['news_post'] = Announcement.objects.exclude(headline=True).order_by('-date')

	return render(request,'post/announcements.html',context_dict)

def competitions(request):

	context_dict = {}
	context_dict['current_page'] = "Competitions"
	#holds the objects for future hackathons 
	context_dict['future_hacks'] = Competition.objects.filter(competition_type='upcoming hack').order_by('-date')
	#holds the objects for the past hackathons 
	context_dict['past_hacks'] = Competition.objects.filter(competition_type='past hacks').order_by('-date')
	
 	return render(request,'post/competitions.html',context_dict)

def calendar(request):
	context_dict = {}
	context_dict['current_page'] = 'Calendar'
	return render(request,'post/calendar.html',context_dict)

def aboutus(request):
	context_dict = {}

	context_dict['current_page'] = "About Us"
	return render(request,'post/about-us.html',context_dict)

def sponsors(request):
	context_dict = {}
	context_dict['current_page'] = 'Sponsors'
	return render(request,'post/sponsors.html',context_dict)
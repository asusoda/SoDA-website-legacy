from django.shortcuts import render
from django.http import HttpResponse
from post.models import Announcement, Competition
is_active = {'announcements':'mdl-layout__tab'}

# Create your views here.
def index(request):
	context_dict = {}
	return render(request,'post/index.html')

def announcements(request):
	#Holds the queries to be dislayed on the front end
	context_dict = {}
	
	#Holds the object for the headline post 
	headline = Announcement.objects.filter(headline=True)
	headline = headline.order_by('-date')
	context_dict['headline'] = headline	
	#Holds the objects that are general announcements 
	news_post = Announcement.objects.exclude(headline=True)
	news_post = news_post.order_by('-date')
	context_dict['news_post'] = news_post

	return render(request,'post/announcements.html',context_dict)

def competitions(request):

	context_dict = {}

	#holds the objects for past hackathons SoDA has went to
	past_travel_hacks = Competition.objects.filter(competition_type='Past Travel Hackathon')
	past_travel_hacks = past_travel_hacks.order_by('-date')
	context_dict['past_travel_hacks'] = past_travel_hacks
	#holds the objects for the current hackathons will travel to
	travel_hack = Competition.objects.filter(competition_type='Current SoDA Travel Hackathon')
	travel_hack = travel_hack.order_by('-date')
	context_dict['travel_hack'] = travel_hack
	#holds the object for the offical SoDA hackathon
	offical_hack = Competition.objects.filter(competition_type='Current Offical SoDA Hackathon')
	offical_hack = offical_hack.order_by('-date')
	context_dict['offical_hack'] = offical_hack
	#holds the objects for past offical SoDA hackathons 
	past_offical_hacks = Competition.objects.filter(competition_type='Past Offical SoDA Coding Competiton')
	past_offical_hacks = past_offical_hacks.order_by('-date')
	context_dict['past_offical_hacks'] = past_offical_hacks	
	#objects for General Hackathons 
	general_hacks = Competition.objects.filter(competition_type='General Hackathons and Coding Competitons')
	general_hacks = general_hacks.order_by('-date')
	context_dict['general_hacks'] = general_hacks
	#objects for past general hackathons	
	context_dict['general_hacks'] = general_hacks
	past_general_hacks = Competition.objects.filter(competition_type='Past General Hackathons and Coding Competitons')
	past_general_hacks = past_general_hacks.order_by('-date')
	context_dict['past_general_hacks'] = past_general_hacks

 	return render(request,'post/competitions.html',context_dict)

def calendar(request):
	return render(request,'post/calendar.html')

def aboutus(request):
	return render(request,'post/about-us.html')

def sponsors(request):
	return render(request,'post/sponsors.html')
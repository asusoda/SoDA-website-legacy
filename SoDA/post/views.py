from django.shortcuts import render
from django.http import HttpResponse
from post.models import Announcement, Competition
#For switch the highlight between tabs
is_active = {'announcements':'mdl-layout__tab','welcome':'mdl-layout__tab','competitions':'mdl-layout__tab','calendar':'mdl-layout__tab','aboutus':'mdl-layout__tab','sponsors':'mdl-layout__tab'}

# Create your views here.
def index(request):
	context_dict = {}
	context_dict.update(is_active)
	context_dict['welcome'] = 'mdl-layout__tab is-active'
	return render(request,'post/index.html',context_dict)

def announcements(request):
	#Holds the queries to be dislayed on the front end
	context_dict = {}
	context_dict.update(is_active)
	context_dict['announcements'] = 'mdl-layout__tab is-active'
	
	context_dict['news_post'] = Announcement.objects.exclude(headline=True).order_by('-date')

	return render(request,'post/announcements.html',context_dict)

def competitions(request):

	context_dict = {}
	context_dict.update(is_active)
	context_dict['competitions'] = 'mdl-layout__tab is-active'
	#holds the objects for past hackathons SoDA has went to
	context_dict['past_travel_hacks'] = Competition.objects.filter(competition_type='Past Travel Hackathon').order_by('-date')
	#holds the objects for the current hackathons will travel to
	context_dict['travel_hack'] = Competition.objects.filter(competition_type='Current SoDA Travel Hackathon').order_by('-date')
	#holds the object for the offical SoDA hackathon
	context_dict['offical_hack'] = Competition.objects.filter(competition_type='Current SoDA Travel Hackathon').order_by('-date')
	#holds the objects for past offical SoDA hackathons 
	context_dict['past_offical_hacks'] = Competition.objects.filter(competition_type='Past Offical SoDA Coding Competiton').order_by('-date')
	#objects for General Hackathons
	context_dict['general_hacks'] = Competition.objects.filter(competition_type='General Hackathons and Coding Competitons').order_by('-date')
	#objects for past general hackathons	
	context_dict['past_general_hacks'] = Competition.objects.filter(competition_type='Past General Hackathons and Coding Competitons').order_by('-dates')

 	return render(request,'post/competitions.html',context_dict)

def calendar(request):
	context_dict = {}
	context_dict.update(is_active)
	context_dict['calendar'] = 'mdl-layout__tab is-active'
	return render(request,'post/calendar.html',context_dict)

def aboutus(request):
	context_dict = {}
	context_dict.update(is_active)
	context_dict['aboutus'] = 'mdl-layout__tab is-active'
	return render(request,'post/about-us.html',context_dict)

def sponsors(request):
	context_dict = {}
	context_dict.update(is_active)
	return render(request,'post/sponsors.html')
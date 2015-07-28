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
	context_dict['current_page'] = "Welcome to SoDA!"
	return render(request,'post/index.html',context_dict)

def announcements(request):
	#Holds the queries to be dislayed on the front end
	context_dict = {}
	context_dict.update(is_active)
	context_dict['announcements'] = 'mdl-layout__tab is-active'
	context_dict['current_page'] = "Newsletter"
	context_dict['news_post'] = Announcement.objects.exclude(headline=True).order_by('-date')

	return render(request,'post/announcements.html',context_dict)

def competitions(request):

	context_dict = {}
	context_dict.update(is_active)
	context_dict['current_page'] = "Competitions"
	context_dict['competitions'] = 'mdl-layout__tab is-active'
	#holds the objects for future hackathons 
	context_dict['future_hacks'] = Competition.objects.filter(competition_type='upcoming hack').order_by('-date')
	#holds the objects for the past hackathons 
	context_dict['past_hacks'] = Competition.objects.filter(competition_type='past hacks').order_by('-date')
	
 	return render(request,'post/competitions.html',context_dict)

def calendar(request):
	context_dict = {}
	context_dict.update(is_active)
	context_dict['current_page'] = 'Calendar'
	context_dict['calendar'] = 'mdl-layout__tab is-active'
	return render(request,'post/calendar.html',context_dict)

def aboutus(request):
	context_dict = {}
	context_dict.update(is_active)
	context_dict['current_page'] = "About Us"
	context_dict['aboutus'] = 'mdl-layout__tab is-active'
	return render(request,'post/about-us.html',context_dict)

def sponsors(request):
	context_dict = {}
	context_dict.update(is_active)
	context_dict['sponsors'] = 'mdl-layout__tab is-active'
	context_dict['current_page'] = 'Sponsors'
	return render(request,'post/sponsors.html')
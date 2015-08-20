from django.db import models
import datetime

# Create your models here.

class Announcement(models.Model):
	
	announcement_title = models.CharField(verbose_name="Title of the Announcement",max_length=100)

	announcement_date = models.DateField(verbose_name="Date of Publication",auto_now_add=False)

	announcement_body = models.TextField(verbose_name="Body of the Announcement")

	announcement_image = models.ImageField(verbose_name="Optional Image for the Announcement",blank=True)

	announcement_location = models.TextField(verbose_name="Optional iFrame map (Set width to auto and height to 486)",blank=True)

	link1 = models.URLField(verbose_name="Optional Link",blank=True)

	link1_name = models.CharField(verbose_name="Optional Link Name",blank=True,max_length=100)

	link2 = models.URLField(verbose_name="Optional Link",blank=True)

	link2_name = models.CharField(verbose_name="Optional Link Name",blank=True,max_length=100)

	def __unicode__(self):
		return self.announcement_title

class Competition(models.Model):

	competition_name = models.CharField(max_length=50,unique=True,verbose_name="Name of the Competition")

	competition_date = models.DateField(verbose_name="Date for the Competition",auto_now_add=False,default=datetime.date.today)

	competition_image =models.ImageField(verbose_name="Optional Card image for the competition",blank=True)

	competiton_basic_information = models.TextField(verbose_name="General Information about the competition")

	competition_website = models.URLField(verbose_name="URL for competition website")

	competition_website_name = models.CharField(verbose_name="Name of the Website",max_length=100)

	competition_map = models.TextField(verbose_name="iFrame for location(Set the width to auto and height to 486)")

	competition_location_info = models.TextField(verbose_name="Location and time for the event")

	travel_information = models.TextField(verbose_name="Information about Traveling to the Event",blank=True)

	travel_map = models.TextField(verbose_name="iFrame map for where we will be meeting to travel to the event",blank=True) 
	#Different types of coding competitons 
	#Used to organize and query database in the view
	TYPE_OF_HACK = (
		('past hacks', 'Past Hackathons/Coding Competitions'),
		('upcoming hack','Future Hackathons/Coding Competitions'),
	)
		
	#Admin can pick what type of coding event 
	competition_type = models.CharField(max_length=50,choices=TYPE_OF_HACK,default='upcoming hacks')
	
	def __unicode__(self):
		return self.competition_name

class Project(models.Model):

	project_title = models.CharField(verbose_name="Project Title",max_length=100)

	project_image = models.ImageField(verbose_name="Optional Image for the project",blank=True)

	project_body = models.TextField(verbose_name="Descriptiong of the project")
	
	git_name = models.CharField(max_length=100,verbose_name="Name of Github repo",blank=True,default="")

	git_link = models.URLField(verbose_name="Link to Github repo",blank=True)

	def __unicode__(self):
		return self.project_title 

class Sponsor(models.Model):

	sponsor_name = models.CharField(max_length=100,verbose_name="Name of Sponsor")
	
	TIERS = (
		('Gold','Gold'),
		('Silver',"Silver"),
		('Bronze','Bronze'),
		)

	sponsorship_tier = models.CharField(max_length=100,verbose_name="Sponsorship Tier",choices=TIERS,default='Gold')

	vector_image = models.ImageField(verbose_name='Image of Company Logo')

	def __unicode__(self):
		return self.sponsor_name
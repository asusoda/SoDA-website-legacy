from django.db import models

# Create your models here.
#Model for updating the annuncements page 
class PostInfo(models.Model):

	title = models.CharField(unique=True,verbose_name="Title of post",max_length=100)

	date = models.DateField(verbose_name="Date of publication",auto_now_add=True)

	body = models.TextField(verbose_name="Text Body of the post")

	location = models.CharField(unique=False,verbose_name="Location of the annuncement")

	location_boolean = models.BooleanField(default=False,verbose_name="Will this post have a location")
	#Test ImageField.height_field/.width_field for the material cards
	image = models.ImageField(default=False)
	#Makes PostInfo Abstract 
	class Meta:
		abstract = True

#Posts card to competition section of the site
#inherits from PostInfo
class Competition(PostInfo):
	
	#Different types of coding competitons 
	#Used to organize and query database in the view
	TYPE_OF_HACK = (
		('Past Travel Hacks', 'Past Travel Hackathon'),
		('Current Travel Hack','Current SoDA Travel Hackathon'),
		('Past Offical SoDA Hack', 'Past Offical SoDA Coding Competiton'),
		('Current Offical SoDA Hack','Current Offical SoDA Hackathon'),
		('General Hacks','General Hackathons and Coding Competitons')
		)
	#Admin can pick what type of coding event 
	competition_type = models.CharField(max_length=50,choices=TYPE_OF_HACK,default='General Hacks')
#Updates the announcements page 
class Announcement(PostInfo):
	#True if post needs to be the headline
	#Organized based on dates
	headline = models.BooleanField()
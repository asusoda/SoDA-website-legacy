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
	image = models.ImageField()

	class Meta:
		abstract = True

	


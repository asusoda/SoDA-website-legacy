from django.contrib import admin
from post.models import Competition,Announcement

# Register your models here.
admin.site.site_header = "SoDA Admin Page!"
admin.site.register(Competition)
admin.site.register(Announcement)
from django.contrib import admin
from post.models import Competition,Announcement,Project,Sponsor

# Register your models here.
admin.site.site_header = "SoDA Admin Page!"
admin.site.register(Competition)
admin.site.register(Announcement)
admin.site.register(Project)
admin.site.register(Sponsor)
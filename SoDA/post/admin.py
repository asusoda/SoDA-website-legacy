from django.contrib import admin
from post.models import Competition,Announcement,Project,Sponsor

class AnnouncementAdmin(admin.ModelAdmin):
	fields =('title','date','body','card_image','link_title','link_url')

class CompetitionAdmin(admin.ModelAdmin):
	fields = ('title','date','body','competition_type','competition_website','competition_website_url','card_image','google_map','link_title','link_url')

class ProjectAdmin(admin.ModelAdmin):
	fields =('title','date','body','card_image','git_name','git_link')

class SponsorAdmin(admin.ModelAdmin):
	fields = ('sponsor_name','sponsorship_tier','vector_image')

# Register your models here.
admin.site.site_header = "SoDA Admin Page!"
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Sponsor,SponsorAdmin)
admin.site.register(Competition,CompetitionAdmin)
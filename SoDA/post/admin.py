from django.contrib import admin
from post.models import Competition,Announcement,Project,Sponsor

class AnnouncementAdmin(admin.ModelAdmin):
	fields =('announcement_title','announcement_date','announcement_body','announcement_image','announcement_location','link1_name','link1','link2_name','link2')

class CompetitionAdmin(admin.ModelAdmin):
	fields = ('competition_name','competition_date','competition_image','competition_basic_information','competition_website_name','competition_website','competition_map','competition_location_info','travel_information','travel_map','competition_type')

class ProjectAdmin(admin.ModelAdmin):
	fields =('project_title','project_post_date','project_image','project_body','git_name','git_link')

class SponsorAdmin(admin.ModelAdmin):
	fields = ('sponsor_name','sponsorship_tier','vector_image')

# Register your models here.
admin.site.site_header = "SoDA Admin Page!"
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Sponsor,SponsorAdmin)
admin.site.register(Competition,CompetitionAdmin)
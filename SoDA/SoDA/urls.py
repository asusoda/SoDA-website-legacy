from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from SoDA import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SoDA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^calendar/',views.calendar,name='calendar'),
    url(r'^about-us/',views.aboutus,name="about-us"),
    url(r'^sponsors/',views.sponsors,name='sponsors'),
) 

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

	urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
from django.conf.urls import patterns, include, url
from django.contrib import admin
from post import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SoDA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/',include('post.urls')),
    url(r'^$',views.index,name='index')
)

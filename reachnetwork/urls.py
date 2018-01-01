from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'reachnetwork.views.home', name='home'),
                       url(r'^home/$', 'reachnetwork.views.home', name='home'),
                       url(r'^members/', include("members.urls")),
                       url(r'^forums/', include("forums.urls")),
                       url(r'^apply/', include("apply.urls")),

                       url(r'^admin/', include(admin.site.urls)),
                       )

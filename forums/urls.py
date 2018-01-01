from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'forums.views.Home'),
                       url(r'^(?P<topic_name>\w+)/$', 'forums.views.topic'),
                       url(r'^(?P<topic_name>\w+)/(?P<post_id>\d+)/$','forums.views.post'),
                       url(r'^(?P<topic_name>\w+)/post/$', 'forums.views.newpost')
                       )

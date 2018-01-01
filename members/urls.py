from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'members.views.Home'),
                       url(r'^register/$',
                           'members.views.SurvivorRegistration', name='register'),
                       url(r'^login/$', 'members.views.LoginRequest',
                           name='login'),
                       url(r'^logout/$', 'members.views.LogoutRequest',
                           name='login'),
                       url(r'^(?P<username>\w+)/$', 'members.views.profile'),
                       )

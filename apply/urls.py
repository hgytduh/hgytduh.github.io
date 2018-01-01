from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'apply.views.contact', name='apply'),
    url(r'^validate/$', 'apply.views.validate', name='validate')
)

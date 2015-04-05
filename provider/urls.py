from django.conf.urls import patterns, url

from provider import views

urlpatterns = patterns('',
                       url(r'^(?P<profile_id>\d+)/$', views.profile, name='profile'),
                       url(r'^login/$', views.profile, name='login'),
                       )
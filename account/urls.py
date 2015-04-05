__author__ = 'rui.b.zhang'

from django.conf.urls import patterns, url
from account import views


urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.login_view, name='login'),
                       url(r'^EditProfile/$', views.edit_user_profile, name='EditProfile'),
                       )
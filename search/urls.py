from django.conf.urls import patterns, url

from search import views

urlpatterns = patterns('',
    url(r'^$',views.search, name='search'),
    #url(r'^(?P<pk>\d+)/$',views.Search.as_view(), name='gosearch'),

    )

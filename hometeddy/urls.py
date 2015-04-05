from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'provider.views.home', name='home'),
                       url(r'^provider/', include('provider.urls', namespace="provider")),
                       url(r'^search/', include('search.urls', namespace="search")),
                       url(r'^dashboard/', include('dashboard.urls', namespace="dashboard")),
                       url(r'^account/', include('account.urls', namespace="account")),
                       # url(r'^service/', 'service.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
                       )
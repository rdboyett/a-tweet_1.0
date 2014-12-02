import os
from  django.conf.urls import *
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.views.static import * 
from django.conf import settings
from django.views.generic import RedirectView
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    
    # Examples:
    #url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)


urlpatterns += patterns('myproject.twitter.views',
    (r'^$', 'index'),
    (r'^a-tweet/$', 'index'),
    (r'^oauth2callback/$', 'auth_return'),
    (r'^test/$', 'test'),
    (r'^dashboard/(?P<classID>\d+)/$', 'dashboard'),
    (r'^dashboard/$', 'dashboard'),
    (r'^myTweets/$', 'myTweets'),
    (r'^search/$', 'search'),
    
    
    #---------------- Ajax Calls --------------------#
    url(r'^tweetSubmit/$', 'tweetSubmit', name='tweetSubmit'),
    url(r'^submitNewClass/$', 'submitNewClass', name='submitNewClass'),
    url(r'^submitJoinClass/$', 'submitJoinClass', name='submitJoinClass'),
    url(r'^submitClassLock/$', 'submitClassLock', name='submitClassLock'),
    url(r'^submitDeleteClass/$', 'submitDeleteClass', name='submitDeleteClass'),
    url(r'^submitDropClass/$', 'submitDropClass', name='submitDropClass'),
    url(r'^submitDeleteTweet/$', 'submitDeleteTweet', name='submitDeleteTweet'),
    url(r'^getNextTweets/$', 'getNextTweets', name='getNextTweets'),
    url(r'^search_bar/$', 'search_bar', name='search_bar'),
    url(r'^sendProfileColors/$', 'sendProfileColors', name='sendProfileColors'),
    url(r'^getNewTweets/$', 'getNewTweets', name='getNewTweets'),
    
)


urlpatterns += staticfiles_urlpatterns()

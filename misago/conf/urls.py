from django.conf import settings
from django.conf.urls import patterns, include, url


_urlpatterns = patterns('misago.conf.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<group_key>(\w|-)+)/$', 'group', name='group'),
)

adminurlpatterns = patterns('misago.conf.views',
    url(r'^settings/', include(_urlpatterns, namespace='settings')),
)
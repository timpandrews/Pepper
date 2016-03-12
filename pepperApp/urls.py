from django.conf.urls import url
from . import views

import pepperApp.views


urlpatterns = [
    url(r'^$', pepperApp.views.testDb_list, name='list'),
    url(r'^create/$', pepperApp.views.testDb_create),
    url(r'^(?P<id>\d+)/$', pepperApp.views.testDb_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', pepperApp.views.testDb_update, name='update'),
    url(r'^(?P<id>\d+)/delete/', pepperApp.views.testDb_delete, name='delete'),
]


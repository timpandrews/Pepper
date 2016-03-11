from django.conf.urls import url
from . import views

import pepperApp.views


urlpatterns = [
    url(r'^$', pepperApp.views.testDb_list),
    url(r'^create/$', pepperApp.views.testDb_create),
    url(r'^(?P<id>\d)/$', pepperApp.views.testDb_detail, name='detail'),
    url(r'^update/$', pepperApp.views.testDb_update),
    url(r'^delete/$', pepperApp.views.testDb_delete),
]


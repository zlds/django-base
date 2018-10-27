# -*- coding: utf-8 -*-
__author__ = 'hancw'
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^getTest1/',views.getTest1),
    url(r'^getTest2/',views.getTest2),
    url(r'^getTest3/',views.getTest3),
    url(r'^postTest1/',views.postTest1),
    url(r'^postTest2/',views.postTest2),
    url(r'^redTest1/',views.redTest1),
    url(r'^redTest2/',views.redTest2),
    url(r'^session1/',views.session1),
    url(r'^session2/',views.session2),
    url(r'^session2_handle/',views.session2_handle),
    url(r'^session3/',views.session3),
    url(r'^(?P<p3>\d+)/(?P<p1>\d+)/(?P<p2>\d+)',views.shuzhi),
    url(r'^(\d+)',views.show)
]

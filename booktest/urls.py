# -*- coding: utf-8 -*-
__author__ = 'hancw'
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)',views.show)
]

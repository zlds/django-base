# -*- coding: utf-8 -*-
__author__ = 'hancw'
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)',views.show),
    url(r'^hello/$',views.hello),
    url(r'^viewArticle/(?P<articleId>\d+)/$',views.viewArticle),
    url(r'^viewArticles/(?P<year>\d{4})/(?P<month>\d{1,2})/$',views.viewArticles,name='articles'),
    url(r'booktest/$',views.booktest,name='book'),
    url(r'test/',views.test),
]

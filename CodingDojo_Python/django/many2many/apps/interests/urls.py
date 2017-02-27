from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^interest/(?P<id>\d+)$', views.sameinterest),
    url(r'^viewpeople$', views.viewpeople),
    url(r'^sameinterest$', views.showme),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^.+$', views.any),
]

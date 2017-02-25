from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^secrets$', views.secrets),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^validate$', views.validate),
]

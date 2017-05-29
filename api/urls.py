"""launduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MachineView, MachineDetailsView, PlaceView, PlaceDetailsView, MachineUserView, MachineUserDetailsView, ReservationView, ReservationDetailsView, FailureView, FailureDetailsView, UserguideView, UserguideDetailsView, AlternativeView, AlternativeDetailsView

urlpatterns = {
    url(r'^machine/$', MachineView.as_view(), name="create"),
    url(r'^machine/(?P<pk>[0-9]+)/$', MachineDetailsView.as_view(), name="details"),


    url(r'^place/$', PlaceView.as_view(), name="create"),
    url(r'^place/(?P<pk>[0-9]+)/$', PlaceDetailsView.as_view(), name="details"),


    url(r'^machineuser/$', MachineUserView.as_view(), name="create"),
    url(r'^machineuser/(?P<pk>[0-9]+)/$', MachineUserDetailsView.as_view(), name="details"),


    url(r'^reservation/$', ReservationView.as_view(), name="create"),
    url(r'^reservation/(?P<pk>[0-9]+)/$', ReservationDetailsView.as_view(), name="details"),


    url(r'^failure/$', FailureView.as_view(), name="create"),
    url(r'^failure/(?P<pk>[0-9]+)/$', FailureDetailsView.as_view(), name="details"),


    url(r'^userguide/$', UserguideView.as_view(), name="create"),
    url(r'^userguide/(?P<pk>[0-9]+)/$', UserguideDetailsView.as_view(), name="details"),


    url(r'^alternative/$', AlternativeView.as_view(), name="create"),
    url(r'^alternative/(?P<pk>[0-9]+)/$', AlternativeDetailsView.as_view(), name="details"),

}

urlpatterns = format_suffix_patterns(urlpatterns)

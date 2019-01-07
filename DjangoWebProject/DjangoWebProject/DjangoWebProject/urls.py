"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import include, url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
import TomisApp.views
from TomisApp.models import Tomis

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', TomisApp.views.index, name='index'),
    url(r'^home$', TomisApp.views.index, name='home'),
    url(r'^ByDevice', TomisApp.views.ByDevice, name='ByDevice'),
    url(r'^ByLocationType', TomisApp.views.ByLocationType, name='ByLocationType'),
    
        
    # url(r'^$', DjangoWebProject.views.home, name='home'),
    # url(r'^DjangoWebProject/', include('DjangoWebProject.DjangoWebProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

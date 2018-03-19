from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^$', views.index),     # This line has changed!
    url(r'^(?P<id>\d+)/$', views.show ),
    url(r'^(?P<id>\d+)/edit', views.edit),
    url(r'^(?P<id>\d+)/delete', views.destroy),
    #number
    #number edit edit number
    #number delete delete redirect ('/')
]
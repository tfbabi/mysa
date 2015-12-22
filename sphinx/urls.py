from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^indexer/(?P<id>[0-9]+)/$', views.indexer, name='indexer'),
]

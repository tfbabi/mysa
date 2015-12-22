from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.stream_response, name='stream_response'),
]

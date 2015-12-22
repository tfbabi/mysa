from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_index, name='login_index'),
    #url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout_account, name='logout_account'),
    url(r'^login/$', views.login_account, name='login_account'),
]

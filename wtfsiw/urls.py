from django.conf.urls import patterns, url

from wtfsiw import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^profile/$', views.profile, name='profile'),
)
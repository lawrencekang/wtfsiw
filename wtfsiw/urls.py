from django.conf.urls import patterns, url

from wtfsiw import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='result'),
    url(r'^retry/$', views.retry, name='retry'),
    url(r'^titleblock_map/$', views.titleblock_map, name='titleblock-map'),
    url(r'^profile/$', views.profile, name='profile'),
)
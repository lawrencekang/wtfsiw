from django.conf.urls import patterns, url

from wtfsiw import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^result/$', views.result, name='result'),

)
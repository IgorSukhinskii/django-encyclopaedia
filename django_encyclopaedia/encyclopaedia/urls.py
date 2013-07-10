from django.conf.urls import patterns, include, url

from encyclopaedia import views


urlpatterns = patterns('',
    url(r'^(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^$', views.index, name='index'),
    url(r'^section/(?P<letter>\w{1})/$', views.section, name='section'),
)

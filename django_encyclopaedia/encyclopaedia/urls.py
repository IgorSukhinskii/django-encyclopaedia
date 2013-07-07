from django.conf.urls import patterns, include, url

from encyclopaedia import views


urlpatterns = patterns('',
    url(r'^(?P<article_id>\d+)/$', views.article, name='article'),
)

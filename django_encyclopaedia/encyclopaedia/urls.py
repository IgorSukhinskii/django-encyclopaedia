from django.conf.urls import patterns, include, url

from encyclopaedia import views


urlpatterns = patterns('',
    # example: /
    url(r'^$', views.index, name='index'),
    # example: section/A/article12/
    url(r'^article(?P<article_id>\d+)/$', views.article, name='article'),
    # example: section/B/
    url(r'^section/(?P<letter>\w{1})/$', views.section, name='section'),
)

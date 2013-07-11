from django.conf.urls import patterns, include, url

from encyclopaedia import views


urlpatterns = patterns('',
    # example: /
    url(r'^$', views.index, name='index'),
    # example: article12/
    url(r'^article(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    # example: section/B/
    url(r'^section/(?P<letter>\w{1})/$', views.section, name='section'),
    url(r'^new/$', views.ArticleCreateView.as_view(), name='article-create'),
    url(r'^article(?P<pk>\d+)/edit/$', views.ArticleUpdateView.as_view(), name='article-update'),
    url(r'^article(?P<pk>\d+)/delete/$', views.ArticleDeleteView.as_view(), name='article-delete'),
)

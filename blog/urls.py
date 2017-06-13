from django.conf.urls import include, url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detail'),
    url(r'^post/new/$', views.post_new, name='new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='edit'),
    url(r'^draft$', views.post_draftlist, name='draft'),    
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]

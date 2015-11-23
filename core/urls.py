from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/', include('registration.backends.simple.urls')),
   url(r'^user/', include('django.contrib.auth.urls')),
   url(r'^post/create/$', PostCreateView.as_view(), name='post_create'),
   url(r'^post/$', PostListView.as_view(), name='post_list'),
   url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
   url(r'^post/update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='post_update'),
   url(r'^post/delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='post_delete'),
   url(r'^post/(?P<pk>\d+)/comment/create/$', CommentCreateView.as_view(), name='comment_create'),
)
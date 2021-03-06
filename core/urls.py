from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/', include('registration.backends.simple.urls')),
   url(r'^user/', include('django.contrib.auth.urls')),
   url(r'^post/create/$', login_required(PostCreateView.as_view()), name='post_create'),
   url(r'^post/$', login_required(PostListView.as_view()), name='post_list'),
   url(r'^post/(?P<pk>\d+)/$', login_required(PostDetailView.as_view()), name='post_detail'),
   url(r'^post/update/(?P<pk>\d+)/$', login_required(PostUpdateView.as_view()), name='post_update'),
   url(r'^post/delete/(?P<pk>\d+)/$', login_required(PostDeleteView.as_view()), name='post_delete'),
   url(r'^post/(?P<pk>\d+)/comment/create/$', login_required(CommentCreateView.as_view()), name='comment_create'),
   url(r'^post/(?P<post_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', login_required(CommentUpdateView.as_view()), name='comment_update'),
   url(r'^post/(?P<post_pk>\d+)/comment/delete/(?P<comment_pk>\d+)/$', login_required(CommentDeleteView.as_view()), name='comment_delete'),
   url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),
   url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
   url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
   url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),
   url(r'^search/$', login_required(SearchPostListView.as_view()), name='search'),
)
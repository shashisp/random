from django.conf.urls import patterns, include, url
from django.contrib import admin
from content.views import ContentListView, VoteFormView, ContentDetailView
from django.contrib.auth.decorators import login_required as auth

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kasturi.views.home', name='home'),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ContentListView.as_view(), name='home'),
    url(r'^content/(?P<slug>[\w-]+)/$', ContentDetailView.as_view(),
    name='content_detail'),
    url(r'^submit/', 'content.views.add_new'),
    url(r'^vote/$', auth(VoteFormView.as_view()), name="vote"),
    url(r'^collections/$', 'content.views.collections'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/', 'content.views.login'),

)

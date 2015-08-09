from django.conf.urls import patterns, include, url
from django.contrib import admin
from content.views import ContentListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kasturi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ContentListView.as_view(), name='home'),
    url(r'^submit/', 'content.views.add_new'),
)

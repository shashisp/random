from django.conf.urls import patterns, include, url
from django.contrib import admin
from content.views import ContentListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kasturi.views.home', name='home'),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ContentListView.as_view(), name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/', 'content.views.login'),
)

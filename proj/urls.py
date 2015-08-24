from django.conf.urls import patterns, include, url
from django.contrib import admin

from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^person', views.view_person, name='view_person'),
    url(r'^rt_search_person', views.quicksearch, name='view_quicksearch'),
    url(r'^admin/', include(admin.site.urls)),
)

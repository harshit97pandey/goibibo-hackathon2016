from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackathon2016.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^v1/checkin-photo/', include('idphotoupload.urls')),

    url(r'^fnr/', include('foodnrestaurant.urls')),

)

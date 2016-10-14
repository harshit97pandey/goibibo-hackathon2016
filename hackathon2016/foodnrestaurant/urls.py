## urls.py

from django.conf.urls import patterns, include, url
from django.contrib import admin
import foodnrestaurant

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackathon2016.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/$','foodnrestaurant.views.test'),
    url(r'^getmenu/(?P<hotelid>\w+)/$','foodnrestaurant.views.get_menu'),
    url(r'^placeorder/(?P<FMN>\w+)/$','foodnrestaurant.views.place_order'),
    url(r'^getorder/(?P<FMN>\w+)/$','foodnrestaurant.views.get_order'),

)
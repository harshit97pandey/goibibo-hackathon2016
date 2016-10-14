## urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # One shot URLs
    url(r'^create/$', views.Uploader.as_view()),
    url(r'^read/$', views.Reader.as_view()),
    url(r'^update/$', views.Updater.as_view()),
    url(r'^delete/$', views.Deleter.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import url
from django.contrib import admin

from .views import Index
app_name = 'mainstat'
urlpatterns = [


    url(r'^$',Index.as_view(),name='index'),
]
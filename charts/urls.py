from django.conf.urls import url
from .views import Charts



urlpatterns = [
    url(r'^$',Charts.as_view(), name='charts'),
]
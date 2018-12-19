from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import RegisterView, BaseView, LoginView,LogOut


app_name = 'accounts'

urlpatterns = [

    #url(r'^jwt/$', obtain_jwt_token),
    #url(r'^$', LoginView.as_view()),   #/base/


    url(r'^login/$', LoginView.as_view(),name='login'),
    url(r'^register/$', RegisterView.as_view(),name='register'),
    url(r'^logout/$', LogOut.as_view(),name='logout'),
]

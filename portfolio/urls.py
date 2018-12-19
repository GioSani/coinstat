from django.conf.urls import url, include


from .views import PortfolioView


app_name = 'portfolio'

urlpatterns = [

    #url(r'^jwt/$', obtain_jwt_token),
    url(r'^$', PortfolioView.as_view(),name="portfolio"),

]

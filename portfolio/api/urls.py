from django.conf.urls import url
from .views import PortfolioAPIView



urlpatterns = [
    url(r'^$', PortfolioAPIView.as_view()),#api/portfolio

]

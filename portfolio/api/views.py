from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins


from .serializer import PortfolioSerializer
from portfolio.models import Portfolio
'''
class PortfolioAPIView(APIView):
    premissin_classes      =[]
    authentication_classes =[]

    def get(self, request, format=None):
        qs = Portfolio.objects.all()
        serializer=PortfolioSerializer(qs,many=True)
        print qs
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Portfolio.objects.all()
        serializer=PortfolioSerializer(qs,many=True)
        return Response(serializer.data)
'''
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication

class PortfolioAPIView(generics.ListAPIView,
                       mixins.CreateModelMixin):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (authentication.JSONWebTokenAuthentication)
    #queryset               =
    serializer_class       =PortfolioSerializer

    def get(self, request, format=None):
        print request.user.id
        qs = Portfolio.objects.filter(user_id=request.user.id)
        #print Portfolio.objects.filter(user_id=request.user.id)
        serializer=PortfolioSerializer(qs,many=True)
        #print qs
        return Response(serializer.data)

    def get_queryset(self):
        qs = Portfolio.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self, request, format=None,*args,**kwargs):
        qs = Portfolio.objects.all()
        serializer=PortfolioSerializer(qs,many=True)
        #print request.data
        return self.create(request,*args,**kwargs)





 
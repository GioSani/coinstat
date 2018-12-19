# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.forms import LoginForm,RegistrationForm
import coinmarketcap


# Create your views here.
class Index(TemplateView):
    initial = {'key': 'value'}
    template_name = 'mainstat\index.html'
    template_name_looged = 'mainstat\index_logged.html'
    #template_name = 'test.html'
    form_login = LoginForm
    form_registration = RegistrationForm
    #template_name = 'mainstat/base.html'

    def get(self,request):
        form_l = self.form_login(initial=self.initial)
        form_r = self.form_registration(initial=self.initial)
        list=[1,2,3]
        market = coinmarketcap.Market()
        coin = market.ticker()

        my_dict={'mylist':coin,'form_r':form_r,'form_l':form_l}
        print 'asd',request.user
        if request.user.is_authenticated():
            print 'logged'
            return render(request,self.template_name_looged,context=my_dict)
        print 'failed'
        return render(request,self.template_name,context=my_dict)

class Logged(TemplateView):
    initial = {'key': 'value'}
    template_name = 'mainstat\index.html'
    template_name_looged = 'mainstat\index_logged.html'
    #template_name = 'test.html'
    form_class = LoginForm
    #template_name = 'mainstat/base.html'

    def get(self,request):
        form = self.form_class(initial=self.initial)
        list=[1,2,3]
        market = coinmarketcap.Market()
        coin = market.ticker()

        my_dict={'mylist':coin,'form':form}
        print 'mainstat:logged',request.user
        if request.user.is_authenticated():
            print 'logged:mainstat'
            return render(request,self.template_name_looged,context=my_dict)
        print 'failed:mainstat'
        return render(request,self.template_name,context=my_dict)


#from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, get_user_model,login
from django.views import View

from .forms import RegistrationForm, LoginForm
import requests
import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.views import logout

class BaseView(TemplateView):
    template_name = "auth_/login.html"

class LogOut(TemplateView):
    template_name = 'mainstat\index.html'
    def post(self, request):
        #print request.session['token']
        logout(request)

        return redirect(reverse('mainstat:index'))

class LoginView(TemplateView):
    #template_name = "mainstat/logged.html"
    template_name = "mainstat/logged.html"
    initial = {'key': 'value'}
    form_class    = LoginForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print 'get function'
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/login/'
        form = self.form_class(request.POST)
        #print form.is_valid()
        #print form.cleaned_data
        print 'asdasd'
        if form.is_valid():
            data = form.cleaned_data
            passed_data = {
            str('username'):str(data['username']),

            str('password'):str(data['password1']),


            }
        #    print passed_data
            headers = {"content-type":"application/json"}

            r = requests.post(AUTH_ENDPOINT,data=json.dumps(passed_data),headers=headers)
            token = r.json()['token']
            token = str(token)
            print token
            user = authenticate(username=str(data['username']),password=str(data['password1']))
            print 'user',user
            if user is not None:
                print 'user is not None'
                login(request, user)
            #print type(token)
            #print token
            request.session['token']=token
            #print request.session['token']
            #print token
            #return HttpResponseRedirect('/success/')
            #print request.user.is_authenticated()
            if user.is_authenticated():
                print 'user is logged'
                print user
                #return redirect(reverse('mainstat:Logged'))
                print 'Logged : LoginVIew'
            #return redirect(name + '/')
            else:
                print 'not logged'


            return redirect(reverse('mainstat:index'))
        else:
            print 'form is not valide'
            print form

        return render(request, self.template_name, {'form': form})




class RegisterView(View):
    form_class = RegistrationForm
    initial = {'key': 'value'}
    template_name = 'mainstat/registered.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print form
        #print form.is_valid()
        if form.is_valid():
            # <process form cleaned data>
            print 'form is valide'
            AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/register/'
            data = form.cleaned_data
            #print data
            passed_data = {
            str('username'):str(data['username']),
            str('email'):str(data['email']),
            str('password'):str(data['password1']),
            str('password2'):str(data['password2']),

            }
            headers = {"content-type":"application/json"}
            r = requests.post(AUTH_ENDPOINT,data=json.dumps(passed_data),headers=headers)
            #print passed_data
            #print r.text
            #return HttpResponseRedirect('/auth/login')
        else:
            print 'data is missing'

        return render(request, self.template_name, {'form': form})


#Social Auth

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'core/home.html')

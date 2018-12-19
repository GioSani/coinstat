# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

import requests
import json
from django.shortcuts import render
from django.views.generic import TemplateView
from forms import PortfolioForm


# Create your views here.
class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"
    initial = {'key': 'value'}
    form_class = PortfolioForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        headers = {"content-type":"application/json"}

        token = request.session['token']
        #print token
        headers = {"content-type":"application/json",
                    "Authorization":"jwt "+ token,

        }
        PORTFOLIO_ENDPOINT = 'http://127.0.0.1:8000/api/portfolio/'
        r = requests.get(PORTFOLIO_ENDPOINT,headers=headers)
        #print r.text[0]
        #print "asd" + r.text


        return render(request, self.template_name, {'context':r.text,'form':form})

    def post(self, request, *args, **kwargs):
        PORTFOLIO_ENDPOINT = 'http://127.0.0.1:8000/api/portfolio/'
        form = self.form_class(request.POST)
        #if form.is_valid():
        print form.is_valid()

        print form
        data = form.cleaned_data
        user_id = request.user.id
        token = request.session['token']
        print token
        #print token
        headers = {"content-type":"application/json",
                    "Authorization":"jwt "+ token,

        }
        passed_data = {'coin_name':data['coin_name'],
                      'coin_quant':data['coin_quant'],
                        'user': user_id
                       }
        data=json.dumps(passed_data)
        r = requests.post(PORTFOLIO_ENDPOINT,headers=headers,data=data)

        return render(request, self.template_name, {'context':r.text,'form':form})

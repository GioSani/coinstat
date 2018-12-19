# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
import coinmarketcap
def symbol_dict():

    market = coinmarketcap.Market()
    coin = market.ticker()
    symbol={}
    for i in coin:
        symbol[i['name']]=i['symbol']

    return symbol


'COINBASE:BTCUSD'

class Charts(TemplateView):

    template_name = 'charts\charts.html'

    def get(self,request):
        other={'MIOTA':'IOT'}
        bittrex_list=['DASH']
        kraken_list=['XRP','EOS','XLM','XMR']
        bitfinx_list = ['TRX','NEO','IOT']
        name=request.GET.get('name')
        #print name
        symbol = symbol_dict()[name]
        #print symbol
        if symbol in kraken_list:
            str='KRAKEN:'+symbol+'USD'
        elif symbol in bitfinx_list:
            str='BITFINEX:'+symbol+'USD'
        elif symbol in other.keys():
            str='BITFINEX:'+other[symbol]+'USD'
        elif symbol in bittrex_list:
            str='BITTREX:'+symbol+'USD'
        else:
            str='COINBASE:'+symbol+'USD'


        return render(request,self.template_name,{'symbol':str})
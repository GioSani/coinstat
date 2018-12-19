from rest_framework import serializers

from portfolio.forms import PortfolioForm
from portfolio.models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = [

        'user',
        'coin_name',
        'coin_quant',
        ]


'''
    def validat_coin_name(self,value):
        if len(value)>15:
            raise serializers.ValidationError('coin_name is way too long')

    def validate(self,data):
        coin_name = data.get('content',None)
        if coin_name == '':
            coin_name = None

        image = data.get('image',None)
        if coin_name is None and coin_quant is None:
            raise serializers.ValidationError("coin name and quantiti is required")
        return data
'''

from rest_framework import serializers 
from tradeTracerApp.models import Stocks, cryptoCurrencies

class StocksSerializer(serializers.ModelSerializer):
 
    class Stock:
        model = Stocks
        fields = ('id',
                  'name',
                  'date',
                  'price')
        
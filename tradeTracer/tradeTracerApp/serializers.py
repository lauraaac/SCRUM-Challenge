from rest_framework import serializers 
from tradeTracerApp.models import Stocks, cryptoCurrencies

class StocksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Stocks
        fields = ('id',
                  'name',
                  'date',
                  'price')
        
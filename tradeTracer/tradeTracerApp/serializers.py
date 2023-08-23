from rest_framework import serializers 
from tradeTracerApp.models import Stocks, Crypto_Currencies

class StocksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Stocks
        fields = ('id',
                  'name',
                  'date',
                  'price')

class CryptoCurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto_Currencies
        fields =('id',
                 'name',
                 'date',
                 'price')

        
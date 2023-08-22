from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tradeTracerApp.models import Stocks, cryptoCurrencies
from tradeTracerApp.serializers import StocksSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def getStocks(request):

    if request.method == 'GET':
        stocks = Stocks.objects.all()        
        nameFilter = request.GET.get("name",None)
        if nameFilter is not None:
            stocks = stocks.filter(name=nameFilter)
        stocksSerializer = StocksSerializer(stocks, many=True)
    return JsonResponse(stocksSerializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def getCrypoCurrencies(request):

    #JSON response for frontend chart testing
    cryptocurrencies = {
    "stock_prices": [
        { "date": '2023-08-17', "price": 80000 },
        { "date": '2023-08-18', "price": 7000 },
        { "date": '2023-08-19', "price": 10000 },
        ]
    }
    
    return JsonResponse(cryptocurrencies)
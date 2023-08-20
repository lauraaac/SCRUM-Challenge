from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tradeTracerApp.models import Stocks, cryptoCurrencies
from tradeTracerApp.serializers import StocksSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def getStocks(request):

    #JSON response for frontend chart testing
    stocks = {
    "stock_prices": [
        { "date": '2023-08-17', "price": 100 },
        { "date": '2023-08-18', "price": 105 },
        { "date": '2023-08-19', "price": 110 },
        ]
    }
    
    return JsonResponse(stocks)


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
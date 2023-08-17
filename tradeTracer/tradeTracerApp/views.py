from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tradeTracerApp.models import Stocks, cryptoCurrencies
from tradeTracerApp.serializers import StocksSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def getStocks(request):
    return None


@api_view(['GET', 'POST', 'DELETE'])
def getCrypoCurrencies(request):
    return None

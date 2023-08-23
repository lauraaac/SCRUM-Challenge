from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tradeTracerApp.models import Stocks, Crypto_Currencies
from tradeTracerApp.serializers import StocksSerializer, CryptoCurrenciesSerializer
from rest_framework.decorators import api_view
from datetime import datetime, timedelta


@api_view(['GET', 'POST', 'DELETE'])
def getStocks(request):

    if request.method == 'GET':
        stocks = Stocks.objects.all().order_by("date")        
        nameFilter = request.GET.get("name",None)
        startDateFilter = request.GET.get("startDate",None)
        finishDateFilter = request.GET.get("finishDate",None)
        
        if nameFilter is not None:
            stocks = stocks.filter(name=nameFilter)
        if startDateFilter is not None and finishDateFilter is not None:
            startDate = datetime.strptime(startDateFilter, "%Y-%m-%d")
            finishDate = datetime.strptime(finishDateFilter, "%Y-%m-%d")
            stocks = stocks.filter(date__gte=startDate, date__lte=finishDate)
        elif startDateFilter is not None and finishDateFilter is None:
            startDate = datetime.strptime(startDateFilter, "%Y-%m-%d")
            stocks = stocks.filter(date__gte=startDate)
        elif startDateFilter is None and finishDateFilter is not None:
            finishDate = datetime.strptime(finishDateFilter, "%Y-%m-%d")
            stocks = stocks.filter(date__lte=finishDate)

        stocksSerializer = StocksSerializer(stocks, many=True)
    return JsonResponse(stocksSerializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def getCrypoCurrencies(request):

    if request.method == 'GET':
        criptoCur = Crypto_Currencies.objects.all().order_by("date")
        print("here")       
        nameFilter = request.GET.get("name",None)
        startDateFilter = request.GET.get("startDate",None)
        finishDateFilter = request.GET.get("finishDate",None)
        
        if nameFilter is not None:
            criptoCur = criptoCur.filter(name=nameFilter)
        if startDateFilter is not None and finishDateFilter is not None:
            startDate = datetime.strptime(startDateFilter, "%Y-%m-%d")
            finishDate = datetime.strptime(finishDateFilter, "%Y-%m-%d")
            criptoCur = criptoCur.filter(date__gte=startDate, date__lte=finishDate)
        elif startDateFilter is not None and finishDateFilter is None:
            startDate = datetime.strptime(startDateFilter, "%Y-%m-%d")
            criptoCur = criptoCur.filter(date__gte=startDate)
        elif startDateFilter is None and finishDateFilter is not None:
            finishDate = datetime.strptime(finishDateFilter, "%Y-%m-%d")
            criptoCur = criptoCur.filter(date__lte=finishDate)

        criptoCurSerializer = CryptoCurrenciesSerializer(criptoCur, many=True)
    
    return JsonResponse(criptoCurSerializer.data,safe=False)
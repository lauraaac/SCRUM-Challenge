from django.urls import path
  
# importing views from views..py
from tradeTracerApp import views
  
urlpatterns = [
    path('stocks/', views.getStocks ),
    path('crypoCurrencies/', views.getCrypoCurrencies),


]
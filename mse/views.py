from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import trades
from chartit import DataPool, Chart

def index(request):
    ticker_list = trades.objects.values('TICKER').order_by('TICKER').distinct()
    context = {'ticker_list': ticker_list}
    return render(request, 'mse/index.html', context) 

def details(request, requested_ticker):
    selected_ticker = trades.objects.order_by('DATE').filter(TICKER=requested_ticker)
    context = {'selected_ticker': selected_ticker, 'requested_ticker': requested_ticker}
    return render(request, 'mse/details.html', context)
    
def chart_view(request, requested_ticker):
    tickerdata = DataPool(
            series=
              [{'options': {
                   'source': trades.objects.order_by('DATE').filter(TICKER=requested_ticker)},
                'terms': [
                   'DATE',
                   'CHANGE',
                   'TRADES',
                   'HIGH',
                   'LOW',
                   'OPEN',
                   'CLOSE']
                 }
               ])
    high_low_close = Chart(
          datasource = tickerdata,
          series_options =
              [{'options':{
                  'type': 'line',
                  'color': 'darkgreen',
                  'stacking': False},
                'terms':{
                  'DATE': [
                       'HIGH']
                    }},
               {'options':{
                  'type': 'line',
                  'stacking': False,
                  #'marker':{ 'enabled': False },
                  'color': 'darkred'},
                'terms': {
                  'DATE': [
                       'LOW']
                }},
               {'options':{
                  'type': 'line',
                  'color': 'lightblue'},
                'terms': {
                  'DATE': [
                       'OPEN']
                }},
               {'options':{
                  'type': 'line',
                  'color': 'orange',
                  'stacking': False},
                'terms': {
                  'DATE': [
                       'CLOSE']
                }}
                 ],
          chart_options =
               {'tooltip': {
                   'shared': True },
                'title': {
                   'text': '%s High/Open/Low/Close' % requested_ticker},
                'xAxis': {
                   'title': {
                       'text': 'Date'},
                       'crosshair': True},
                'yAxis': {
                   'title': {
                       'text': 'Amount'},
                       'crosshair':True}})


    trades_chart = Chart(
           datasource = tickerdata,
           series_options =
               [{'options':{
                   'type': 'line',
                   'color': 'black',
                   'stacking': False},
                 'terms':{
                   'DATE': [
                        'TRADES']
                     }}],
           chart_options =
                {'tooltip': {
                    'shared': 'true'},
                 'title': {
                    'text': '%s Trades' % requested_ticker},
                 'xAxis': {
                    'title': {
                        'text': 'Date'},
                        'crosshair': True},
                 'yAxis': {
                    'title': {
                        'text': 'Trades'},
                        'crosshair': True}})


    change_chart = Chart(
           datasource = tickerdata,
           series_options =
               [{'options':{
                   'type': 'line',
                   'color': 'black',
                   'stacking': False},
                 'terms':{
                   'DATE': [
                        'CHANGE']
                     }}],
           chart_options =
                {'tooltip': {
                    'shared': 'true' },
                 'title': {
                    'text': '%s Change' % requested_ticker},
                 'xAxis': {
                    'title': {
                        'text': 'Date'},
                        'crosshair': True},
                 'yAxis': {
                    'title': {
                        'text': 'Change'},
                        'crosshair': True}})

    return render(request,'mse/chart.html', {'charts': [high_low_close, trades_chart, change_chart],'requested_ticker': requested_ticker})

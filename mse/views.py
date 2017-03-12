from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import trades
from chartit import DataPool, Chart
from investments.utils import get_links

def index(request):
    ticker_list = trades.objects.values('ticker').order_by('ticker').distinct()
    links = get_links(request.path)
    context = {'ticker_list': ticker_list, 'links': links}
    return render(request, 'mse/index.html', context) 

def details(request, requested_ticker):
    selected_ticker = trades.objects.order_by('date').filter(ticker__iexact=requested_ticker)
    links = get_links(request.path)
    context = {'selected_ticker': selected_ticker, 'requested_ticker': requested_ticker, 'links': links}
    return render(request, 'mse/details.html', context)
    
def chart_view(request, requested_ticker):
    tickerdata = DataPool(
            series=
              [{'options': {
                   'source': trades.objects.order_by('date').filter(ticker=requested_ticker)},
                'terms': [
                   'date',
                   'change',
                   'trades',
                   'high',
                   'low',
                   'open',
                   'close',
                   'volume'],
                 }
               ])
    high_low_close = Chart(
          datasource = tickerdata,
          series_options =
              [{'options':{
                  'type': 'line',
                  'color': '#000000',
                  'stacking': False},
                'terms':{
                  'date': [
                       'high']
                    }},
               {'options':{
                  'type': 'line',
                  'stacking': False,
                  'color': '#FF0000'},
                'terms': {
                  'date': [
                       'low']
                }},
               {'options':{
                  'type': 'line',
                  'stacking': False,
                  'color': '#00FF00'},
                'terms': {
                  'date': [
                       'open']
                }},
               {'options':{
                  'type': 'line',
                  'color': 'orange',
                  'stacking': False},
                'terms': {
                  'date': [
                       'close']
                }},
                 ],
          chart_options =
               {'tooltip': {
                   'shared': True },
                'credits': {
                   'enabled': False },
                'title': {
                   'text': '%s High/Open/Low/Close' % requested_ticker},
                'xAxis': {
                   'title': {
                       'text': 'Date'},
                       'crosshair': True},
                'yAxis': {
                   'title': {
                       'text': 'Amount'},
                       'crosshair':True},
                'plotOptions':{
                   'series':{
                       'marker':{
                           'enabled': False,
                           'symbol': 'circle',
                           'radius': 1}}}})


    trades_chart = Chart(
           datasource = tickerdata,
           series_options =
               [{'options':{
                   'type': 'line',
                   'color': 'black',
                   'stacking': False},
                 'terms':{
                   'date': [
                        'trades']
                     }}],
           chart_options =
                {'tooltip': {
                    'shared': 'true'},
                 'credits': {
                    'enabled': False},
                 'title': {
                    'text': '%s Trades' % requested_ticker},
                 'xAxis': {
                    'title': {
                        'text': 'Date'},
                        'crosshair': True},
                 'yAxis': {
                    'title': {
                        'text': 'Trades'},
                        'crosshair': True},
                 'plotOptions':{
                        'series':{
                            'marker':{
                               'symbol': 'circle',
                               'radius': 1,
                               'enabled': False}}}})


    change_chart = Chart(
           datasource = tickerdata,
           series_options =
               [{'options':{
                   'type': 'line',
                   'color': 'black',
                   'stacking': False},
                   'terms':{
                     'date': [
                          'change']
                       }}],
           chart_options =
                {'tooltip': {
                    'shared': 'true' },
                 'credits': {
                    'enabled': False},
                 'title': {
                    'text': '%s Change' % requested_ticker },
                 'xAxis': {
                    'title': {
                        'text': 'Date'},
                    'crosshair': True},
                 'yAxis': {
                    'title': {
                        'text': 'Change'},
                    'crosshair': True,
                    'plotLines': [{
                        'value': 0,
                        'zIndex': '3'
                        }]},
                 'plotOptions': {
                    'series': {
                        'color': '#000000',
                        'marker': {
                           'symbol': 'circle',
                           'radius': 1,
                           'color': '#000000',
                           'enabled': False}}}})
    
    volume_chart = Chart(
           datasource = tickerdata,
           series_options =
               [{'options':{
                   'type': 'line',
                   'color': 'black',
                   'stacking': False},
                 'terms':{
                   'date': [
                        'volume']
                      }}],
           chart_options=
               {'title': {
                   'text': '%s Volume' % requested_ticker},
                'credits': {
                    'enabled': False},
                'xAxis': {
                    'title': { 'text': 'Date' },
                    'crosshair': True},
                'yAxis': {
                    'title': { 'text': 'Volume' },
                    'crosshair': True},
                'plotOptions':{
                    'series':{
                        'marker':{
                              'symbol': 'circle',
                              'radius': 1,
                              'enabled': False}}}})

    links = get_links(request.path)

    context = {'charts': [high_low_close, trades_chart, change_chart, volume_chart], 'requested_ticker': requested_ticker, 'links': links}
    return render(request,'mse/chart.html', context)

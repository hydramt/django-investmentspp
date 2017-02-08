from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^(?P<requested_ticker>[A-Za-z0-9]+)/$', views.details, name='details'),
   url(r'^(?P<requested_ticker>[A-Za-z0-9]+)/chart/$', views.chart_view, name='chart'),
]

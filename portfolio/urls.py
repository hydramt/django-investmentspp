"""investments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin, auth
from django.contrib.auth import views as auth_view
from django.shortcuts import render
from . import views
from homedata.views import index as homedata_index, login_bar as homedata_loginbar

urlpatterns = [
    url(r'^$', views.index, name='portfolio_index'),
    url(r'^add/$', views.add, name='add_portfolio'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^del/$', views.del_port, name='delete_portfolio'),
    url(r'^del_post/$', views.del_post, name="del_post"),
    url(r'^view/(?P<portfolio_id>[0-9]+)/$', views.view_portfolio, name='view_portfolio'),
    url(r'^view/(?P<portfolio_id>[0-9]+)/add_portfolio_data/$', views.add_portfolio_data, name='add_portfolio_data'),
]

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from homedata import models

@login_required(login_url='login')
def lgd_in(request):
    username = request.POST.get('id_username')
    password = request.POST.get('id_password')
    user = authenticate(username=username, password=password)
    return render(request, 'investments/logged_in.html')

def lgd_out(request):
    logout(request)
    return HttpResponse("You have been logged out.")

from homedata.models import exchanges

def index(request):
    exch_list = exchanges.objects.values('EXCH_FULL','EXCH').order_by('EXCH_FULL').distinct()
    context = { 'exch_list': exch_list }
    return render(request, 'homedata/index.html', context)


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def lgd_in(request):
    username = request.POST.get('id_username')
    password = request.POST.get('id_password')
    user = authenticate(username=username, password=password)
    return render(request, 'investments/logged_in.html')

def lgd_out(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next','/'))

def account(request):
    return HttpResponse("Account")

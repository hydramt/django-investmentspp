from django.shortcuts import render
from homedata.models import exchanges
from django.contrib.auth.decorators import login_required

def index(request):
    exch_list = exchanges.objects.filter(ENABLED=1).values('EXCH_FULL','EXCH').order_by('EXCH_FULL').distinct()
    context = { 'exch_list': exch_list }
    return render(request, 'homedata/index.html', context)

def login_bar(request):
    return render(request, 'homedata/login_bar.html')

@login_required
def profile(request):
    return render(request, 'portfolio/portfolio.html')


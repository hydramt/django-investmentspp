from django.shortcuts import render
from homedata.models import exchanges
from django.contrib.auth.decorators import login_required
from investments.utils import get_links

def index(request):
    exch_list = exchanges.objects.filter(enabled=1).values('exch_full','exch').order_by('exch_full').distinct()
    links = get_links(request.path)
    context = { 'exch_list': exch_list, 'links': links }
    return render(request, 'homedata/index.html', context)

def login_bar(request):
    return render(request, 'homedata/login_bar.html')

@login_required
def profile(request):
    context = {'links': get_links(request.path)}
    return render(request, 'portfolio/portfolio.html', context)


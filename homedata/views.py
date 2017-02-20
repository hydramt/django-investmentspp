from django.shortcuts import render
from homedata.models import exchanges
from django.contrib.auth.decorators import login_required
from investments.utils import get_links

def index(request):
    exch_list = exchanges.objects.filter(ENABLED=1).values('EXCH_FULL','EXCH').order_by('EXCH_FULL').distinct()
    links = get_links(request.path)
    context = { 'exch_list': exch_list, 'links': links }
    return render(request, 'homedata/index.html', context)

def login_bar(request):
    return render(request, 'homedata/login_bar.html')

@login_required
def profile(request):
    return render(request, 'portfolio/portfolio.html')


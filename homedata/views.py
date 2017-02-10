from django.shortcuts import render
from .models import exchanges

def index(request):
    exch_list = exchanges.objects.values('EXCH_FULL','EXCH').order_by('EXCH_FULL').distinct()
    context = { 'exch_list': exch_list }
    return render(request, 'homedata/index.html', context)


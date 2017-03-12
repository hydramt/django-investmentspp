from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import portfolio
from investments.utils import get_links

@login_required(login_url='/login')
def index(request):
    user_id = request.user.id
    portfolios = portfolio.objects.values('portfolio_id','portfolio_name').filter(user_id=user_id)
    context = {'links': get_links(request.path), 'portfolios': portfolios } 
    return render(request, 'portfolio/portfolio.html', context)


def add(request):
    context = {'links': get_links(request.path)}
    return render(request, 'portfolio/add.html', context)

@login_required()
def add_post(request):
    portfolio_name = request.POST.get('portfolio_name')
    new_portfolio = portfolio(user_id=request.user.id, portfolio_name=portfolio_name)
    new_portfolio.save()
    context = {'message': 'Portfolio %s has been added.' % (portfolio_name),'links': get_links(request.path)}
    return render(request, 'portfolio/success.html', context) 

@login_required()
def del_port(request):
    user_id = request.user.id
    portfolios = portfolio.objects.values('portfolio_id', 'portfolio_name').filter(user_id=user_id)
    context = {'links': get_links(request.path), 'portfolios': portfolios}
    return render(request, 'portfolio/del.html', context)

@login_required()
def del_post(request):
    portfolio_id = request.POST.get('delportfolio')
    del_portfolio = portfolio.objects.get(portfolio_id=portfolio_id)
    del_portfolio.delete()
    context = {'message': 'Portfolio %s has been deleted.' % (portfolio_id), 'links': get_links(request.path)}
    return render(request, 'portfolio/success.html', context)

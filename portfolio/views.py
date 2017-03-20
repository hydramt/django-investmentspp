from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import portfolio, portfolio_data
from investments.utils import get_links
from django.db.models import Sum

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

@login_required
def view_portfolio(request, portfolio_id):
	holdings = portfolio_data.objects.values('security_id').filter(user_id=request.user.id, portfolio_id=portfolio_id).order_by('security_id').distinct()
	summary = []
	for x in holdings:
		summary.append(portfolio_data.objects.filter(portfolio_id=portfolio_id, security_id=x['security_id']).aggregate(Sum('quantity')))
	breakdown = portfolio_data.objects.values('security_id','quantity').filter(portfolio_id=portfolio_id, user_id=request.user.id).order_by('security_id')
	nicebreakdown = []
	bd_str = ''
	i=0
	import pdb
	for x in range(0,len(holdings)):
		for z in breakdown:
			if z['security_id'] == holdings[i]['security_id']:
				bd_str+="<tr><td class=\"breakdown-col1\">Security:</td><td>%s</td><td>Quantity:</td><td class=\"breakdown-col2\">%s</td></tr>" % (z['security_id'],z['quantity'])
		nicebreakdown.append(bd_str)
		bd_str = ''
		i+=1
	#pdb.set_trace()
	data = zip(holdings, summary, nicebreakdown)
	context = {'portfolio_id': portfolio_id, 'data': data, 'links': get_links(request.path), 'breakdown': breakdown, 'nicebreakdown': nicebreakdown}
	return render(request, 'portfolio/view.html', context)

@login_required
def add_portfolio_data(request, portfolio_id):
    user_id=request.user.id
    security_id=request.POST.get('security_id')
    date=request.POST.get('date')
    quantity=request.POST.get('quantity')
    purchase_price=request.POST.get('purchase_price')
    if request.POST.get('expenses') != '':
      expenses=request.POST.get('expenses')
    else:
      expenses=None
    new_data = portfolio_data(portfolio_id=portfolio_id, user_id=user_id, security_id=security_id, date=date, quantity=quantity, purchase_price=purchase_price, expenses=expenses)
    new_data.save()
    return redirect(view_portfolio, portfolio_id=portfolio_id)

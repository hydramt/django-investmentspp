from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import portfolio, portfolio_data
from investments.utils import get_links
from django.db.models import Sum
from mse.models import trades

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
	portfolio_name = portfolio.objects.values('portfolio_name').filter(portfolio_id=portfolio_id)
	summary = []
	total = []
	total_value = int() 
	for x in holdings:
		try:
			close=trades.objects.values('close').filter(ticker=x['security_id']).order_by('-id')[0]['close']
		except IndexError:
			close={'close': 'N/A'}
		quantity=portfolio_data.objects.filter(portfolio_id=portfolio_id, security_id=x['security_id'], user_id=request.user.id).aggregate(quantity=Sum('quantity'))['quantity']
		try:
			current_value=close*quantity
		except TypeError:
			current_value='N/A'
		summary.append(portfolio_data.objects.filter(portfolio_id=portfolio_id, security_id=x['security_id']).aggregate(Sum('quantity')))
		total.append(current_value)
		try:
			total_value+=current_value
		except TypeError:
			pass
	breakdown = portfolio_data.objects.values('security_id','quantity','purchase_price','expenses').filter(portfolio_id=portfolio_id, user_id=request.user.id).order_by('security_id')
	nicebreakdown = []
	bd_str = ''
	i=0
	import pdb
	for x in range(0,len(holdings)):
		for z in breakdown:
			if z['security_id'] == holdings[i]['security_id']:
				if z['expenses'] is None:
					expenses = 0.00;
				else:
					expenses = z['expenses']
				bd_str+="<tr><td class=\"breakdown-label1\">Security:</td><td class=\"breakdown-value1\">%s</td><td class=\"breakdown-label2\">Quantity:</td><td class=\"breakdown-value2\">%s</td><td class=\"breakdown-label3\">Purchase price:</td><td class=\"breakdown-value3\">%s</td><td class=\"breakdown-label4\">Expenses:</td><td class=\"breakdown-value4\">%s</td></tr>" % (z['security_id'],z['quantity'],z['purchase_price'],expenses)
		nicebreakdown.append(bd_str)
		bd_str = ''
		i+=1
	#pdb.set_trace()
	data = zip(holdings, summary, nicebreakdown, total)
	context = {'portfolio_name': portfolio_name, 'data': data, 'links': get_links(request.path), 'breakdown': breakdown, 'nicebreakdown': nicebreakdown, 'total_value': total_value}
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

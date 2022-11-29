from django.shortcuts import render, get_object_or_404, redirect
from user.models import Subscription
from django.core.paginator import Paginator


def index(request):
	subs = Subscription.objects.all().order_by('-id')
	p = Paginator(subs, 10)
	page_num = request.GET.get('page', 1)
	page = p.page(page_num)
	context = {
		"subs": page,
	}
	return render(request, 'admin_kaspi/subscriptions/subscriptions.html', context)


def add(request):
	return render(request, 'admin_kaspi/subscriptions/add.html')


def create(request):
	if request.method == 'POST':
		sub = Subscription(title=request.POST['title'],
						   period=request.POST['period'],
						   price=request.POST['price'])
		
		sub.save()
		return redirect('admin_subscription_index')


def edit(request, id):
    sub = get_object_or_404(Subscription, id=id)
    return render(request, 'admin_kaspi/subscriptions/edit.html', {'subscription': sub})


def update(request, id):
	if request.method == 'POST':
		sub = get_object_or_404(Subscription, id=id)
		sub.__dict__.update(title=request.POST['title'],
						    period=request.POST['period'],
						    price=request.POST['price'])
		sub.save()
		return redirect('admin_subscription_index')


def delete(request, id):
	sub = get_object_or_404(Subscription, id=id)
	sub.delete()
	return redirect('admin_subscription_index')
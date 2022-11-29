import openpyxl
import pandas
from django.shortcuts import render, redirect, get_object_or_404
from user.models import User
from django.contrib.auth import login as log_in
from user.models import Subscription
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from cabinet.service import read_user_pricelist, parse_table, save_rows_in_file
from django.conf import settings
import os
from django.core.paginator import Paginator
from datetime import timedelta
import asyncio
from django.contrib import messages


def account(request):
	return redirect('pricelist')


def pricelist(request):
	if request.user.check_active():
		page_num = request.GET.get('page', 1)
		search = request.GET.get('search', '')
		data = read_user_pricelist(user=request.user, offset=int(page_num) - 1, search=search)
		if not data:
			context = {}
		else:
			fake_rows = [None] * data['amount_rows']
			p = Paginator(fake_rows, 20)
			page_num = request.GET.get('page', 1)
			page = p.page(page_num)

			context = {
				'data': data,
				'page': page,
				'search': search,
			}
	else:
		subscriptions = Subscription.objects.all().order_by('-id')
		context = {
			'subscriptions': subscriptions
		}
	return render(request, 'pricelist.html', context)


def pricelist_update(request):
	if request.method == 'POST':
		request.user.pricelist = request.FILES['pricelist']

		wookbook = openpyxl.load_workbook(request.FILES['pricelist'])
		worksheet = wookbook.active
		if worksheet.max_column > 10:
			messages.info(request, "Неверный формат прайслиста. Проверьте его с шаблоном.")
			return redirect('pricelist')

		request.user.save()

		return redirect('pricelist')
	return render(request, 'pricelist_update.html')


def pricelist_save(request):
	if request.method == 'POST':
		html = request.POST['table']
		rows = parse_table(html)

		if not request.user.pricelist:
			return redirect('pricelist')

		file = os.path.join(settings.MEDIA_ROOT, request.user.pricelist.name)
		save_rows_in_file(file, rows)

	return redirect('pricelist')


def user_settings(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		user.username = request.POST['username']
		user.email = request.POST['email']
		user.telegram_id = request.POST['telegram_id']
		user.kaspi_login = request.POST['kaspi_login']
		user.kaspi_password = request.POST['kaspi_password']
		user.kaspi_company = request.POST['kaspi_company']
		user.kaspi_merchant_id = request.POST['kaspi_merchant_id']
		user.skip_merchant_id = request.POST['skip_merchant_id']

		if request.POST['password']:
			user.set_password(request.POST['password'])

		user.save()
		log_in(request, user)
		return redirect('user_settings')
	else:
		return render(request, 'user_settings.html')


def pay(request, id):
	subscription = get_object_or_404(Subscription, id=id)
	if subscription.free():
		request.user.active = True
		request.user.active_date = timezone.now() + timedelta(days=subscription.period)
		request.user.save()
	return redirect('pricelist')

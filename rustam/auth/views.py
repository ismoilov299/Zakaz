from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out, login as log_in
from user.models import User


def login(request):
	if request.user.is_authenticated:
		return redirect('account')

	password = request.POST['password']
	user = User.objects.filter(email=request.POST['email'])

	if user:
		user = user[0]
		if user.check_password(password):
			log_in(request, user)
			if user.is_superuser:
				return redirect('admin_index')
			return redirect('account')
	return redirect('index')


def sign_up(request):
	user = User.objects.filter(email=request.POST['email'])
	if user:
		return redirect('index')

	user = User(username=request.POST['username'],
				email=request.POST['email'],)
	user.set_password(request.POST['password'])
	user.save()
	log_in(request, user)
	return redirect('account')


def logout(request):
	log_out(request)
	return redirect('index')

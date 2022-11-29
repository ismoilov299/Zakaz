from django.shortcuts import render, get_object_or_404, redirect
from user.models import User
from django.core.paginator import Paginator
from datetime import datetime


def admin_index(request):
	return redirect('admin_user_index')


def index(request):
	users = User.objects.all().order_by('-id')
	p = Paginator(users, 10)
	page_num = request.GET.get('page', 1)
	page = p.page(page_num)
	context = {
		"users": page,
	}
	return render(request, 'admin_kaspi/users/users.html', context)


def add(request):
	return render(request, 'admin_kaspi/users/add.html')


def create(request):
	if request.method == 'POST':
		user = User(username=request.POST['username'],
				    email=request.POST['email'],
				    active=request.POST['active'])
		user.set_password(request.POST['password'])
		user.save()

		if request.POST['role'] == 'admin':
			user.is_superuser = True
		else:
			user.is_superuser = False
		
		user.save()

		return redirect('admin_user_index')


def edit(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'admin_kaspi/users/edit.html', {'user': user})


def update(request, id):
	if request.method == 'POST':
		user = get_object_or_404(User, id=id)
		user.__dict__.update(username=request.POST['username'], 
							 email=request.POST['email'],
						     active=request.POST['active'],
						     active_date=datetime.strptime(request.POST['active_date'], '%Y-%m-%d')
						     )

		if request.POST['role'] == 'admin':
			user.is_superuser = True
		else:
			user.is_superuser = False

		user.save()

		return redirect('admin_user_index')


def delete(request, id):
	user = get_object_or_404(User, id=id)
	user.delete()
	return redirect('admin_user_index')
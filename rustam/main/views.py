from django.shortcuts import render, redirect


def index(request):
	if request.user.is_authenticated:
		return redirect('account')
	return render(request, 'index.html')


def handler404(request, exception=None):
	return render(request, 'errors/404.html')
	
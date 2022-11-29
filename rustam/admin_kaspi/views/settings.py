from django.shortcuts import render, get_object_or_404, redirect
from main.models import Setting


def index(request):
    return render(request, 'admin_kaspi/settings/settings.html')


def update(request):
	if request.method == 'POST':
		setting = Setting.get_settings()
		setting.__dict__.update(copyright=request.POST['copyright'],
								token=request.POST['token'], 
							 	tag=request.POST['tag'],)
		setting.save()
		return redirect('admin_settings_index')

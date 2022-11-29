from main.models import Setting


def context_controller(request):
	settings = Setting.get_settings()
	context = {
		'settings': settings,
	}
	return context

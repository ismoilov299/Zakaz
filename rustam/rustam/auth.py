from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class CheckAuth(MiddlewareMixin):
	def process_request(self, request, *args, **kwargs):
		path = request.get_full_path()
		if 'admin' in path:
			if not request.user.is_authenticated or not request.user.is_superuser:
				return redirect('index')

		if 'account' in path:
			if not request.user.is_authenticated:
				return redirect('index')
		
		return None
		
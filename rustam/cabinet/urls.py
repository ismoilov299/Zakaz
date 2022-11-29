from django.urls import path

from . import views as cabinet

urlpatterns = [
	path('', cabinet.account, name='account'),
	path('pricelist/', cabinet.pricelist, name='pricelist'),
	path('pricelist/update', cabinet.pricelist_update, name='pricelist_update'),
	path('pricelist/save', cabinet.pricelist_save, name='pricelist_save'),
	path('user_settings/', cabinet.user_settings, name='user_settings'),
	path('pay/<id>/', cabinet.pay, name='pay'),
]
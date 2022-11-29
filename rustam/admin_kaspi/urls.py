from django.urls import path

from .views import users, settings, subscriptions

urlpatterns = [
    path('', users.admin_index, name="admin_index"),

    path('settings/', settings.index, name="admin_settings_index"),
    path('settings/update/', settings.update, name="admin_settings_update"),

	path('users/', users.index, name="admin_user_index"),
    path("users/add/", users.add, name="admin_user_add"),
    path("users/create/", users.create, name="admin_user_create"),
    path("users/edit/<id>/", users.edit, name="admin_user_edit"),
    path("users/update/<id>/", users.update, name="admin_user_update"),
    path("users/delete/<id>/", users.delete, name="admin_user_delete"),

    path('subscriptions/', subscriptions.index, name="admin_subscription_index"),
    path("subscriptions/add/", subscriptions.add, name="admin_subscription_add"),
    path("subscriptions/create/", subscriptions.create, name="admin_subscription_create"),
    path("subscriptions/edit/<id>/", subscriptions.edit, name="admin_subscription_edit"),
    path("subscriptions/update/<id>/", subscriptions.update, name="admin_subscription_update"),
    path("subscriptions/delete/<id>/", subscriptions.delete, name="admin_subscription_delete"),
]

from django.urls import path

from . import views as auth

urlpatterns = [
    path("login/", auth.login, name="login"),
    path("sign-up/", auth.sign_up, name="sign_up"),
    path('logout/', auth.logout, name="logout"),
]
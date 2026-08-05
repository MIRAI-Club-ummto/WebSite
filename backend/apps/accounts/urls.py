from django.urls import path
from .views import LoginView, LogoutView, MeView

urlpatterns = [
    path("login/",  LoginView.as_view(),  name="account-login"),
    path("logout/", LogoutView.as_view(), name="account-logout"),
    path("me/",     MeView.as_view(),     name="account-me"),
]

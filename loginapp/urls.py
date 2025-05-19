from django.urls import path
from django.contrib import admin
from .views import SignupView, LoginView, UserView

urlpatterns = [
    path('', UserView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
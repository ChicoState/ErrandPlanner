
from django.urls import include, path
from app import views as app_views
from . import views

urlpatterns = [
    path('join/', views.join),
    path('login/', views.user_login),
]
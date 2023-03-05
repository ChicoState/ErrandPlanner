from django.urls import include, path
from app import views as app_views

urlpatterns = [
    path('errands/', app_views.errands)
]
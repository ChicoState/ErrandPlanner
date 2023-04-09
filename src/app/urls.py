
from django.urls import include, path

# from app import views as app_views
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("join/", views.join),
    path("login/", views.user_login),
    path("calendar/", views.calendar),
    path("calendar/add/", views.addEvent),
    path("", views.errands),
    path("<str:pk>", views.delete_errand, name="nothing"),
    path("errands/", views.errands),
    path("errands/<str:pk>", views.delete_errand, name="nothing"),
    path("errands/add/", views.addErrand),
    path("errands/edit/<int:id>/", views.editErrand),
]
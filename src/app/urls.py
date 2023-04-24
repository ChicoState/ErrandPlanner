from django.urls import include, path

# from app import views as app_views
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.login, name="Login"),
    path("auth/", views.auth, name="auth"),
    path("calendar/", views.calendar, name="Calendar"),
    path("calendar/add/", views.addEvent, name="AddEvent"),
    path("", views.errands, name="Home"),
    path("errands/", views.errands, name="Errands"),
    path("errands/add/", views.addErrand, name="AddErrand"),
    path("errands/edit/<int:id>/", views.editErrand),
    path("errands/<str:pk>", views.delete_errand, name="DeleteErrand"),
]

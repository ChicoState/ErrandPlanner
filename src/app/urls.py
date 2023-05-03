from django.urls import include, path

# from app import views as app_views
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("auth/", views.auth, name="auth"),
    path("", views.errands, name="home"),
    path("errands/", views.errands, name="errands"),
    path("errands/add/", views.addErrand, name="add_errand"),
    path("errands/edit/<int:id>/", views.editErrand),
    path("errands/completed/<int:id>/", views.completeErrand),
    path("errands/<str:pk>", views.deleteErrand, name="delete_errand"),
]

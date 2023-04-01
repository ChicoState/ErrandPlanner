<<<<<<< HEAD
from django.urls import path
from . import views


urlpatterns = [    
    path('errands', views.errands),
]

# I believe that this is the correct urls.py
# path('name of the page youre trying to view', views.(name of the funcntion that youre trying to implament))
=======

from django.urls import include, path
# from app import views as app_views
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('join/', views.join),
    path('login/', views.user_login),
    path('calendar/', views.calendar),
    path('', views.errands),
    path('errands/', views.errands),
    path('errands/add/', views.addErrand),
    # path('errands/edit/', views.editErrand),
    path('errands/edit/<int:id>/', views.editErrand)
]
>>>>>>> c14185165227038064188a86e56973bdb242ffdd

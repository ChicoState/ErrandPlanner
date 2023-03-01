from django.urls import path
from . import views


urlpatterns = [    
    path('errands', views.errands),
]

# I believe that this is the correct urls.py
# path('name of the page youre trying to view', views.(name of the funcntion that youre trying to implament))
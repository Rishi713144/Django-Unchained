
from django.urls import path

from . import views

urlpatterns = [
    
    path ('', views.all_newapp , name='all_newapp'),
    path ('home/', views.home , name='home'),
    
]

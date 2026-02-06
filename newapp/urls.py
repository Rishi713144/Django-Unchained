
from django.urls import path

from . import views

urlpatterns = [
    
    path ('', views.all_newapp , name='all_newapp'),
    path ('<int:newapp_id>/', views.newapp_detail , name='newapp_detail'),
    path ('home/', views.home , name='home'),
    
]

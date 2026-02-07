from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_newapp, name='all_newapp'),
    path('home/', views.home, name='home'),
    path('stories/', views.newapp_stories, name='newapp_stories'),
    path('<int:newapp_id>/', views.newapp_detail, name='newapp_detail'),
]

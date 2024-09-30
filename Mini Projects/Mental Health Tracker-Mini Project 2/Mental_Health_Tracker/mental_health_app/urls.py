from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('mood/', views.mood_entries, name='mood_entries'),
    path('sessions/', views.therapy_sessions, name='therapy_sessions'),
    path('resources/', views.resources, name='resources'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]


from generator import views

from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('password_generated/', views.password, name='password'),
    path('about/', views.about, name='about'),
]

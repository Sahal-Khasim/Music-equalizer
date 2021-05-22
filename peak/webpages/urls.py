from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='home'),
    path('home/', views.home, name='intro'),
]

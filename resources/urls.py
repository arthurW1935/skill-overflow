from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('cpp/', views.cpp, name='cpp'),
    path('webdev/', views.webdev, name='webdev'),
    path('machinelearning/', views.machinelearning, name='machinelearning'),
    path('about/', views.about, name="about")
]

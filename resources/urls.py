from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('cpp/', views.cpp, name='cpp'),
    path('html/', views.html, name='html'),
    path('css/', views.css, name='css'),
    path('javascript/', views.javascript, name='javascript'),
    path('c', views.c, name='c'),
    path('csharp/', views.csharp, name='csharp'),
    path('webdev/', views.webdev, name='webdev'),
    path('datascience/', views.datascience, name='datascience'),
    path('machinelearning/', views.machinelearning, name='machinelearning'),
    path('appdev/', views.appdev, name='appdev'),
    path('about/', views.about, name="about")
]

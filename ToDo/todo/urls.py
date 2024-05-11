"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllToDos.as_view(), name='index'),
    path('today/', views.TodayToDo.as_view(), name='today'),
    path('mark_complete/<int:pk>/', views.mark_complete, name='mark_complete'),
    path('mark_incomplete/<int:pk>/', views.mark_incomplete, name='mark_incomplete'),
    path('del_task/<int:pk>/', views.del_task, name='del_task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
]

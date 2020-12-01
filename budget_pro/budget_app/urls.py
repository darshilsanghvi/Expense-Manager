from django.contrib import admin
from django.urls import path,include
from budget_app import views

urlpatterns = [
        path('home/',views.home_page),]
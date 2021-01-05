from django.contrib import admin
from django.urls import path,include, register_converter
from budget_app import views
from datetime import datetime

class DateConverter:
      regex = r'\d{4}-\d{2}-\d{2}'

      def to_python(self, value):
            return datetime.strptime(value, '%Y-%m-%d')
      
      def to_url(self, value):
            return value

register_converter(DateConverter, 'yyyy')


urlpatterns = [
        path('home/',views.home_page),
        path('home/add_expense', views.add_expense),
        path('home/change_budget/', views.change_budget),
        path('home/delete/<int:pk>', views.delete_expense),
        path('home/date/2020-12-12', views.show_dates),
        path('home/date/<yyyy:date>/', views.show_dates),
            ]
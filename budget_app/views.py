from django.shortcuts import render, redirect
from .models import expense, budget
from datetime import datetime, timedelta
import datetime
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np

def home_page(request):
    today = datetime.date.today()
    weekday = today.weekday()
    start_delta = datetime.timedelta(days=weekday)
    start_of_week = today - start_delta
    week_dates = []
    for day in range(1,8):
        week_dates.append(start_of_week - datetime.timedelta(days=day))
    date = request.POST.get('date','')
    all_expenses = expense.objects.filter(expense_date=date)
    return redirect('/budget/home/')
    latest = budget.objects.last()
    context = {'all_expenses':all_expenses,'latest':latest, 'week_dates':week_dates, 'today':today}
    return render(request, 'budget_app/home.html', context)

def add_expense(request):
    today_date = str(datetime.date.today().strftime('20%y-%m-%d'))
    today_day = str(datetime.date.today().strftime('%A'))
    latest = budget.objects.last()
    if request.method=='POST':
        name = request.POST.get('name','')
        amnt = request.POST.get('amnt','')
        etype = request.POST.get('type','')
        day = request.POST.get('day','')
        date = request.POST.get('date','')
        expe = expense(expense_name=name,expense_amnt=amnt,expense_type=etype,expense_day=day,expense_date=date) 
        expe.save()
        latest.left_budget = latest.left_budget - int(amnt)
        latest.save()
        return redirect('/budget/home/')
    all_expenses = expense.objects.all()
    context = {'today_date':today_date,'today_day':today_day,'latest':latest,
              'all_expenses':all_expenses}
    return render(request, 'budget_app/add_exp.html', context)

def change_budget(request):
    if request.method=='POST':
        monthly_income =  request.POST.get('budget','')
        budgets_data = budget.objects.all()
        for i in budgets_data:
            if int(monthly_income) > i.total_budget:
                i.left_budget = i.left_budget+(int(monthly_income)-i.total_budget)
                i.total_budget = int(monthly_income)
            elif int(monthly_income) < i.total_budget:
                i.left_budget = i.left_budget+(i.total_budget-int(monthly_income))
                i.total_budget = int(monthly_income)
            i.save()
        return redirect('/budget/home/')
    return render(request, 'budget_app/change_budget.html')


def delete_expense(request, pk):
    if request.method=='POST':
        i = expense.objects.get(pk = pk)
        budgets_data = budget.objects.get(pk = 1)
        budgets_data.left_budget = budgets_data.left_budget + i.expense_amnt
        budgets_data.save()
        i.delete()
        return redirect('/budget/home/')
    return render(request, "budget_app/delete.html")


from django.shortcuts import render, redirect
from .models import expense, budget
from datetime import datetime, timedelta
import datetime


def home_page(request):
    #week_list = []
    today_date = str(datetime.date.today().strftime('20%y-%m-%d'))
    #for i in range(1,8):
     #   week_list.append(datetime.date.today()-timedelta(i))
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
    return render(request, 'budget_app/base.html', context)


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
    return render(request, 'budget_app/home.html')


def delete_expense(request, pk):
    if request.method=='POST':
        i = expense.objects.get(pk = pk)
        budgets_data = budget.objects.get(pk = 1)
        budgets_data.left_budget = budgets_data.left_budget + i.expense_amnt
        budgets_data.save()
        i.delete()
        return redirect('/budget/home/')
    return render(request, "budget_app/delete.html")
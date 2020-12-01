from django.shortcuts import render
from .models import expense
import datetime
def home_page(request):
    today_date = str(datetime.date.today().strftime('20%y-%m-%d'))
    today_day = str(datetime.date.today().strftime('%A'))
    if request.method=='POST':
        name = request.POST.get('name','')
        amnt = request.POST.get('amnt','')
        etype = request.POST.get('type','')
        day = request.POST.get('day','')
        date = request.POST.get('date','')
        expe = expense(expense_name=name,expense_amnt=amnt,expense_type=etype,expense_day=day,expense_date=date) 
        expe.save()
    all_expenses = expense.objects.all()
    context = {'today_date':today_date,'today_day':today_day,
                    'all_expenses':all_expenses}
    return render(request, 'budget_app/home.html', context)

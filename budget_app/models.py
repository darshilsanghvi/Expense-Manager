from django.db import models

class expense(models.Model):
    expense_name = models.CharField(max_length=40)
    expense_type = models.CharField(max_length=40)
    expense_amnt = models.IntegerField()
    expense_day = models.CharField(max_length=15)
    expense_date = models.CharField(max_length=20)
    
class budget(models.Model):
    total_budget = models.IntegerField()
    left_budget = models.IntegerField()


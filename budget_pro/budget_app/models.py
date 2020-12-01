from django.db import models

class expense(models.Model):
    expense_name = models.CharField(max_length=40)
    expense_type = models.CharField(max_length=40)
    expense_amnt = models.IntegerField()
    expense_day = models.CharField(max_length=15)
    expense_date = models.DateField(auto_now=False)



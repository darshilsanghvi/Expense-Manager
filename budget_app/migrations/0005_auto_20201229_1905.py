# Generated by Django 3.1a1 on 2020-12-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0004_auto_20201210_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='left_budget',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='total_budget',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]

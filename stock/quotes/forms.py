from django import forms
from django.forms import fields
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
            model = Stock
            fields = ["ticker"]
from django.shortcuts import redirect, render
from .models import Stock
#from djangostock.stock.quotes.models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3b2b7dea6591476892c2c05fed85979e")

        try: 
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api':api})

    else:
        return render(request, 'home.html', {'ticker':"Enter A Ticker Symbol Above..."})




def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added Successfully"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item)  + "/quote?token=pk_3b2b7dea6591476892c2c05fed85979e")
            try: 
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output })

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ( str(item) + " has Successfully been Deleted"))
    return redirect(delete_stock)


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})
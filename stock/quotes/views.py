from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    # pk_3b2b7dea6591476892c2c05fed85979e
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_3b2b7dea6591476892c2c05fed85979e")

    try: 
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."


    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})
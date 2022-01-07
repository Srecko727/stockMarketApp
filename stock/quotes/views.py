from django.shortcuts import render

# Create your views here.

def home(request):
    # pk_3b2b7dea6591476892c2c05fed85979e
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
from django.shortcuts import render
# Create your views here.

def index(request):
    data = {
        'title': 'home'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
    
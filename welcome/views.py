from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'TimeTracker'}
    return render(request, 'welcome/index.html', context)
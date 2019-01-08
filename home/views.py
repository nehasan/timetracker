from django.shortcuts import render

from django.contrib.auth.models import User

from attendances.models import Attendance

# Create your views here.

def index(request):
    context = {'title': 'Home'}
    return render(request, 'home/index.html', context)

def check_in(request):
    current_user = request.user
    context = {'title': 'Home'}
    return render(request, 'home/index.html', context)

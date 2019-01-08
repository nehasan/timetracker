from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'Attendance'}
    return render(request, 'attendances/index.html', context)

def show(request):
    context = {'title': 'Attendance'}
    return render(request, 'attendances/show.html', context)

def create(request):
    context = {'title': 'Attendance'}
    return render(request, 'attendances/show.html', context)

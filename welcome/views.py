from django.shortcuts import render

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    logger.log(request.user)
    context = {'title': 'TimeTracker'}
    return render(request, 'welcome/index.html', context)

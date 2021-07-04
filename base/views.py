from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


def index(request):

    context = {
    }
    return render(request, 'base/index.html', context)

# catch none defined requests
def handler404(request, exception, template_name="404.html"):
    return render(request, 'base/404.html')

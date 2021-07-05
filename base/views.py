from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .forms import ModifiedForm

def index(request):

    if request.method == "POST":
        form = ModifiedForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_fact= form.cleaned_data['auth_fact']
    else:
        form = ModifiedForm()
    return render('admin/login.html',{'form':ModifiedForm})

def handler404(request):
    return 1

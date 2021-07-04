from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


def handler404(request, exception, template_name="404.html"):
    raise Http404("Page not fount")

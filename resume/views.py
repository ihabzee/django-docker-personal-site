from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    globals = Section.objects.filter(type=Section.GLOBAL)
    personals = Section.objects.filter(type=Section.PERSONAL)
    experiances = Section.objects.filter(type=Section.EXPERIANCE)
    educations = Section.objects.filter(type=Section.EDUCATION)
    others = Section.objects.filter(type=Section.OTHER)
    context = {
        'globals' : globals,
        'personals' : personals,
        'experiances' : experiances,
        'educations' : educations,
        'others' : others
    }
    return render(request, 'resume/index.html', context)

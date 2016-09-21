from django.http import HttpResponse
from django.shortcuts import render

from .models import Subject


def index(request):
    subjects_list = Subject.objects.order_by('name')
    context = {
        'subjects_list': subjects_list,
    }
    return render(request, 'scheduler/index.html', context)

def generate(request):
    return HttpResponse("SECTION RESPONSIBLE FOR PLAN GENERATING")

def data(request):
    return HttpResponse("SECTIONS RESPONSIBLE FOR ADDING DATA")

def restrict(request):
    return HttpResponse("SECTIONS RESPONSIBLE FOR REESTRICTIONS")

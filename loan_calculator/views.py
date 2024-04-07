from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loan_calculator(request):
    return HttpResponse("Hello loan_calc!")
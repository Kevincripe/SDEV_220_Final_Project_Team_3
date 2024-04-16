from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loan_calculator(request):
    return HttpResponse("Hello loan_calc!")

def loan_calc_results(request):
    return render(request, 'loan_calculator/loan_calc_results.html', {})

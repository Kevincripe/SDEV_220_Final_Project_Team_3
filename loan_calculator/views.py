from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import LoanCalculator

# Create your views here.

def loan_calculator(request):
    return HttpResponse("Hello loan_calc!")

def loan_calc_results(request):
    calculations = LoanCalculator.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'loan_calculator/loan_calc_results.html', {'calculations':calculations})


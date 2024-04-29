from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import LoanCalculator

# Create your views here.

def loan_calculator(request):
    return HttpResponse("Hello loan_calc!")

def loan_calc(request):
    calculations = LoanCalculator.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'loan_calculator/loan_calc.html', {'calculations':calculations})

def result(request):
    down_payment = float(request.GET.get('down_payment'))
    interest_rate = float(request.GET.get('interest_rate'))
    num_of_months = int(request.GET.get('num_of_months'))
    loan_amount = float(request.GET.get('loan_amount'))

    if request.GET.get('interest_rate') == "0":
        ans = (loan_amount - down_payment) / num_of_months
        
    elif request.GET.get('interest_rate') >= "0":    
        ans = '0'

    return render(request, 'loan_calculator/result.html', {'ans': ans})

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
    # Checking if Interest rate field is Zero
    if request.GET.get('interest_rate') == "0":
        # no interest means simple calculation
        monthly_payment = (loan_amount - down_payment) / num_of_months 
        return render(request, 'loan_calculator/result.html', {'monthly_payment': monthly_payment, 'total_paid': loan_amount, 'total_interest': '0'} )
        
    # If interest is invovled have to calc monthly interest and compute
    elif request.GET.get('interest_rate') >= "0": 
        monthly_interest_rate = interest_rate / 1200  
        monthly_payment = (loan_amount * monthly_interest_rate ) / (1-(1 + monthly_interest_rate)**(- num_of_months))
        total_paid = monthly_payment * num_of_months
        total_interest = total_paid - loan_amount
        return render(request, 'loan_calculator/result.html', \
            {'monthly_payment': monthly_payment, 'total_paid': total_paid, 'total_interest': total_interest})

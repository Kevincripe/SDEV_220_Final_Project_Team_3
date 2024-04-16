from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, You are at the sales lead index")

def sales_lead_list(request):
    return render(request, 'sales_leads/sales_lead_list.html', {})


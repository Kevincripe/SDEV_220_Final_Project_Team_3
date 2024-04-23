from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import SalesLead

# Create your views here.
def index(request):
    return HttpResponse("Hello, You are at the sales lead index")

def sales_lead_list(request):
    sales = SalesLead.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sales_leads/sales_lead_list.html', {'sales':sales})

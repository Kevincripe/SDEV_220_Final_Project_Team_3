from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sales_leads(request):
    return HttpResponse("Hello sales_leads!")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employees_vendors(request):
    return HttpResponse("Hello emp_vend!")



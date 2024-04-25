from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import EmployeeVendor

# Create your views here.
def employees_vendors(request):
    return HttpResponse("Hello emp_vend!")

def employees_vendors_list(request):
    vendors = EmployeeVendor.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'employees_vendors/employees_vendors_list.html', {'vendors':vendors})


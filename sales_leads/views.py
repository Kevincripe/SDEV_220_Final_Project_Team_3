from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import SalesLead
from django.contrib.auth.decorators import login_required
from .forms import SalesForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("Hello, You are at the sales lead index")

# Sales lead page is locked to Admin management only
# Sales rep's need to clear with floor mgr to remove

@login_required
def sales_lead_list(request):
    sales = SalesLead.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sales_leads/sales_lead_list.html', {'sales':sales})

@login_required
def post_new(request):
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            SalesLead = form.save(commit=False)
            SalesLead.author = request.user
            SalesLead.published_date = timezone.now()
            SalesLead.save()
            return redirect('sales_lead_list')

    else:
        form = SalesForm
    
    return render(request, 'sales_leads/post_new.html', {'form': form})

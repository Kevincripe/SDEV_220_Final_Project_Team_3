from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import SoldUnits
from django.contrib.auth.decorators import login_required
from .forms import SoldForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("Hello, You are at the sold units index")

@login_required
def sold_units_list(request):
    sold = SoldUnits.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sold_units/sold_units_list.html', {'sold':sold})

@login_required
def sold_new(request):
    if request.method == "POST":
        form = SoldForm(request.POST)
        if form.is_valid():
            SoldUnits = form.save(commit=False)
            SoldUnits.author = request.user
            SoldUnits.published_date = timezone.now()
            SoldUnits.save()
            return redirect('sold_units_list')

    else:
        form = SoldForm
    
    return render(request, 'sold_units/sold_new.html', {'form': form})

from django.shortcuts import render
from .models import *
from .forms import * 
# Create your views here.
def input(request):
    form = ClaimForm
    if request.method == 'POST': 
        print(request.POST) 
        form = ClaimForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("form is saved")
            form.save() 
            return render(request, 'main/successful.html')
        else:
            return render(request, 'main/unsuccessful.html')
    context = {'form': form} 
    return render(request, 'main/form.html', context)

def dash(request):
    return render(request, 'main/dashboard.html')

def inspect(request):
    return render(request, 'main/inspect.html')
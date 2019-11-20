from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def indexView(request):
#     return render(request, 'index.html')
#
# def dashboardView(request):
#     return render(request, 'dashboard.html')

def registerView(request):
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})

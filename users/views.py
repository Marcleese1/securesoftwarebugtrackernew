from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

# def indexView(request):
#     return render(request, 'index.html')
#
# def dashboardView(request):
#     return render(request, 'dashboard.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            success_url = reverse_lazy('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})


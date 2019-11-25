from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.contrib.auth import login, logout


# Create your views here.

# def indexView(request):
#     return render(request, 'index.html')
#
# def dashboardView(request):
#     return render(request, 'dashboard.html')



# class signup(CreateView):
#     form_class = UserRegisterForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')
def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

    else:
        form = UserRegisterForm()
    return render(request, 'registration/login.html', {'form':form})


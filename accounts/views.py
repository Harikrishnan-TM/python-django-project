from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from django.urls import reverse
from accounts.forms import CustomUserCreationForm

def home(request):
    return HttpResponse('Home page')

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('register'))
    return render(request, 'accounts/register.html', {'form': form})
    
    
def loginpage(request):
    return HttpResponse('loginpage')
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login!')
            form.save()
            return redirect('login')
        else:
            messages.error(request, f'Fehler beim Account erstellen!')
            return redirect('register')
            
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myapp.forms import UserCreationForm
from django.contrib.auth import authenticate, login


@login_required(login_url='login')
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
    return render(request, 'login.html')

@login_required(login_url='login')
def landing_view(request):
    return render(request, 'landing.html')

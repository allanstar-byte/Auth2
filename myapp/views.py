from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myapp.forms import UserCreationForm

@login_required(login_url='admin:login')
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

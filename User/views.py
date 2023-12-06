from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('admin')
        else:
            messages.error(request,'Username or Password is incorrect')
            return redirect('login')
    else:
        return render(request, 'registration/login.html',{})

def signupView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password1')
            login(request, authenticate(request, username=username, password=password))
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html',{
        'form': form,
    })

def logoutView(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('login')
# Create your views here.

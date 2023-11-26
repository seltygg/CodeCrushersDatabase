from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .backends import CustomBackend
from .models import Accounts
from datetime import datetime
from django.db.models import Max
def login_view(request):
    # return render(request, 'registration/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, login=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('success_page')  # Change 'success_page' to the name of your success page URL
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'registration/login.html')

def success_page_view(request):
    return render(request, 'registration/success_page.html')

def signup_view(request):
    if request.method == 'POST':
        accountemail = request.POST.get('accountemail')
        accountpassword = request.POST.get('accountpassword')
        accountphonenum = request.POST.get('accountphonenum')

        try:
            # Get the latest accountid
            latest_account = Accounts.objects.aggregate(Max('accountid'))
            latest_account_id = latest_account['accountid__max']

            # Increment the accountid
            if latest_account_id:
                new_account_id = 'AC' + str(int(latest_account_id[2:]) + 1).zfill(8)
            else:
                new_account_id = 'AC00000001'

            # Validate and create the user
            user = Accounts.objects.create(
                accountid=new_account_id,
                accountemail=accountemail,
                accountpassword=accountpassword,
                accountphonenum=accountphonenum,
                accountdate=datetime.now()
            )

            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to login after successful signup
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')

    return render(request, 'registration/signup.html')

# def login_view(request):
#   if request.method == 'POST':
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       return redirect('home')
#   return render(request, 'registration/login.html')
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import LoginForm
#from .models import CustomUser


def logon_admin(request):
    messages = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
       
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_active :
             
                login(request, user)
                if user.role == 0:
                    role_select = 'user_panel'
                elif user.role == 1:
                    role_select = 'admin_panel'
                return redirect(f'{role_select}')
            else:
                messages = 'User or password incorect'
    else:
        form = LoginForm()
      
    content = {
        'form': form,
        'messages': messages,
    }
    
    return render(request, 'admin.html', content)
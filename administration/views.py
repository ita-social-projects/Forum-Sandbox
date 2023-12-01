from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from profiles.models import Profile



def logon_admin(request):
    messages = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                role_select = 'info'
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

@login_required
def info(request):
    users = CustomUser.objects.all()
    companys = Profile.objects.all()
    content = {
        'users' : users,
        'companys' : companys,
    }
    return render(request,'admin_info.html', content)
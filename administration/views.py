from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from authentication.models import *
from profiles.models import *



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

@login_required
def approve_company(request):
    saved_companies = SavedCompany.objects.all()

    user_info_list = []
    not_approved_info_list = []

    for company in saved_companies:
        user_info = {
            'email': company.user.email,
            'name': company.user.name,
            'edrpou': company.company.edrpou,
            'profile_name': company.company.name,
            'is_active ': company.company.is_registered,
        }

        if not company.company.is_registered:
            not_approved_info_list.append(user_info)
        elif company.company.is_registered:
            user_info_list.append(user_info)    

    content = {
        'user_info_list': user_info_list,
        'not_approved_info_list': not_approved_info_list,
    }
    return render(request, 'admin_approve_company.html', content)

@login_required
def search(request):
    content = {
    }
    return render(request,'admin_settings.html', content)

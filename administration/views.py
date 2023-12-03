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

    approved_info_list = []
    not_approved_info_list = []

    for user_company in saved_companies:
        user_info = {
            'email': user_company.user.email,
            'name_company_owner': user_company.user.name,
            'edrpou': user_company.company.edrpou,
            'company_name': user_company.company.name,
            'is_active ': user_company.company.is_registered,
            'is_deleted': user_company.company.is_deleted,
            'id': user_company.company.id
        }

        if not user_company.company.is_registered:
            not_approved_info_list.append(user_info)
        elif user_company.company.is_registered:
            approved_info_list.append(user_info)    

    content = {
        'approved_info_list': approved_info_list,
        'not_approved_info_list': not_approved_info_list,
    }
    return render(request, 'admin_approve_company.html', content)

@login_required
def search(request):
    content = {
    }
    return render(request,'admin_settings.html', content)

@login_required
def erdpou_aproved(request, id):
    my_object = SavedCompany.objects.get(company_id = id)
    my_object.company.is_registered = True 
    my_object.company.save() 
    return  redirect('approve_company')


@login_required
def company_unregistered(request, id):
    my_object = SavedCompany.objects.get(company_id = id)
    my_object.company.is_registered = False 
    my_object.company.save() 
    return  redirect('approve_company')



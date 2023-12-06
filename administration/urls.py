from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Login logic
    path('administrator/', views.logon_admin, name='admin_panel'),
    path('administrator/info/', login_required(views.info), name = 'info'),
    path('administrator/logout/', auth_views.LogoutView.as_view(next_page='admin_panel'), name='logout'),
    path('administrator/approve_company/', login_required(views.approve_company), name = 'approve_company'),
    path('administrator/approve_company/erdpou/<int:id>/', login_required(views.erdpou_aproved), name = 'erdpou_aproved'),
    path('administrator/approve_company/unregistered/<int:id>/', login_required(views.company_unregistered), name = 'company_unregistered'),
    path('administrator/search/', login_required(views.search), name = 'search'),
    path('administrator/company/<int:id>/', login_required(views.admin_full_company_info), name = 'admin_full_company_info'),

]
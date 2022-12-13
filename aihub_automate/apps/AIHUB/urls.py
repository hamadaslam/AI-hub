

from django.urls import path, re_path
from apps.AIHUB import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # The home page
    path('', views.index, name='Index'),
    path('home/', views.home, name='home'),
    path('editprofile/', views.editprofile, name='editProfile'),
    path('companyDetails/', views.companyDetails, name='companyDetails'),
    path('companyDetails/<int:company_id>', views.companyDetails, name='companyDetails'),
    path('companylist/', views.companylist, name='companyDetails'),
    path('projectDetails/<int:company_id>', views.projectDetails, name='projectDetails'),
    path('companycash/<int:project_id>', views.companycash, name='CompanyCash'),
    path('projectdetailsview/<int:company_id>', views.projectdetailsview, name='projectdetailsview'),
    path('projects/<int:company_id>', views.projects, name='projects'),
    path('projectinfo/<int:projectid>', views.projectinfo, name='projectinfo'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),  
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("password_change/", views.password_change, name="password_change"),
    path("projectinfoform/<int:projectid>",views.projectinfoform, name = 'projectinfoform'),
    path("workplan/<int:projectiinfoform_id>",views.workplan, name = 'workplan'),
    path("teammembers/<int:projectiinfoform_id>",views.teammembers, name = 'teammembers'),
    path("projectinfopi/<int:projectid>",views.projectinfopi, name = 'projectinfoPI'),
    path("sendforms/<int:company_id>",views.sendforms, name = 'sendforms'),
    path("changestatus/<int:company_id>",views.changestatus, name = 'status'),
    path('companylistscope/', views.companylistscope, name='companyDetails'),
    path('addnotes/<int:company_id>', views.addnotes, name='notes'),
    path('changeprojectstatus/<int:projectid>/<int:company_id>', views.changeprojectstatus, name='notes'),
    path('sendapprovalforms/<int:projectid>', views.sendapprovalforms, name='approvalform'),
    

]

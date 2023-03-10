"""DC_Finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
#adding finance team dashboard
    path('', views.dashboard, name='dashboard'),

    path('research_centre/', views.research_center, name='research_center'),
    path('Add_Research_Centre/', views.Add_Research_Centre, name='Add_Research_Centre'),

#Adding all render page url here
    path('project_partner/', views.project_partner, name='project_partner'),
    path('fiscal_year/', views.fiscal_year, name='fiscal_year'),
    path('department/', views.department, name='department'),
    path('program/', views.program, name='program'),
    path('faculty/', views.faculty, name='faculty'),
    path('project/', views.project, name='project'),
    path('funder/', views.funder, name='funder'),
    path('naics_classification/', views.naics_classification, name='naics_classification'),
    path('review/', views.review, name='review'),
    path('finance/', views.finance, name='finance'),
    path('student/', views.student, name='student'),
    path('funding_level/', views.funding_level, name='funding_level'),
    path('industry_size/', views.industry_size, name='industry_size'),
    path('resource/', views.resource, name='resource'),

#adding all form urls here
path('Add_project_partner/', views.Add_project_partner, name='Add_project_partner'),
path('Add_fiscal_year/', views.Add_fiscal_year, name='Add_fiscal_year'),
path('Add_department/', views.Add_department, name='Add_department'),
path('Add_program/', views.Add_program, name='Add_program'),
path('Add_faculty/', views.Add_faculty, name='Add_faculty'),
path('Add_project/', views.Add_project, name='Add_project'),
path('Add_funder/', views.Add_funder, name='Add_funder'),
path('Add_naics_classification/', views.Add_naics_classification, name='Add_naics_classification'),
path('Add_review/', views.Add_review, name='Add_review'),
path('Add_finance/', views.Add_finance, name='Add_finance'),
path('Add_student/', views.Add_student, name='Add_student'),
path('Add_funding_level/', views.Add_funding_level, name='Add_funding_level'),
path('Add_industry_size/', views.Add_industry_size, name='Add_industry_size'),
path('Add_resource/', views.Add_resource, name='Add_resource'),
path('Resource_dropdown_update/', views.Resource_dropdown_update, name='Resource_dropdown_update'),
]

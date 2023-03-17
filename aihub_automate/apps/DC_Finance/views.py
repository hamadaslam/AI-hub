from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.template.loader import get_template
from django.http import HttpResponse 
from django.http import JsonResponse
import json
from django.core import serializers


# Create your views here.
def dashboard(request):
    context = {'segment': 'dashboard',}

    html_template = get_template('DC_Finance/index2.html')
    return HttpResponse(html_template.render(context, request))


#view to view research centres in the db
def research_center(request):
    research_center = RESEARCH_CENTRE.objects.filter()
    return render(request, 'DC_Finance/research_center.html', {'research_center': research_center})

# creating add research page to add new research centres to the db
def Add_Research_Centre(request):
    if request.method == "POST":
        form = RESEARCH_CENTRE_FORM(request.POST)
        if form.is_valid():
            Research_Centre = form.save(commit=False)
            Research_Centre.save()
            return redirect('/fin/research_centre',)
    else:
        form = RESEARCH_CENTRE_FORM()
    return render(request, 'DC_Finance/Add_Research_Centre.html', {'form': form})


#creating all views to see the db in the front end

def project_partner(request):
    project_partner = PROJECT_PARTNER.objects.filter()
    return render(request, 'DC_Finance/project_partner.html', {'project_partner': project_partner})

def fiscal_year(request):
    fiscal_year = FISCAL_YEAR.objects.filter()
    return render(request, 'DC_Finance/fiscalyear.html', {'fiscal_year': fiscal_year})

def department(request):
    department = DEPARTMENT.objects.filter()
    return render(request, 'DC_Finance/department.html', {'department': department})

def program(request):
    program = Program.objects.filter()
    return render(request, 'DC_Finance/programs.html', {'program': program})

def faculty(request):
    faculty = FACULTY.objects.filter()
    return render(request, 'DC_Finance/faculty.html', {'faculty': faculty})

def project(request):
    project = Project.objects.filter()
    return render(request, 'DC_Finance/projects.html', {'project': project})

def funder(request):
    funder = FUNDER.objects.filter()
    return render(request, 'DC_Finance/funders.html', {'funder': funder})

def naics_classification(request):
    naics_classification = NAICS_CLASSIFICATION.objects.filter()
    return render(request, 'DC_Finance/naics_classification.html', {'naics_classification': naics_classification})

def review(request):
    review = REVIEW.objects.filter()
    return render(request, 'DC_Finance/reviews.html', {'review': review})

def finance(request):
    finance = FINANCE.objects.filter()
    return render(request, 'DC_Finance/finance.html', {'finance': finance})

def student(request):
    student = STUDENT.objects.filter()
    return render(request, 'DC_Finance/students.html', {'student': student})

def funding_level(request):
    funding_level = FUNDING_LEVEL.objects.filter()
    return render(request, 'DC_Finance/funding_level.html', {'funding_level': funding_level})

def industry_size(request):
    industry_size = INDUSTRY_SIZE.objects.filter()
    return render(request, 'DC_Finance/industry_size.html', {'industry_size': industry_size})

def resource(request):
    resource = RESOURCE.objects.filter()
    return render(request, 'DC_Finance/resources.html', {'resource': resource})


#creating all views for forms
# creating add research page to add new research centres to the db
def Add_project_partner(request):
    if request.method == "POST":
        form = PROJECT_PARTNER_FORM(request.POST)
        if form.is_valid():
            PROJECT_PARTNER = form.save(commit=False)
            PROJECT_PARTNER.save()
            return redirect('/fin/project_partner',)
    else:
        form = PROJECT_PARTNER_FORM()
    return render(request, 'DC_Finance/Add_project_partner.html', {'form': form})

def Add_fiscal_year(request):
    if request.method == "POST":
        form = FISCAL_YEAR_FORM(request.POST)
        if form.is_valid():
            FISCAL_YEAR = form.save(commit=False)
            FISCAL_YEAR.save()
            return redirect('/fin/fiscal_year',)
    else:
        form = FISCAL_YEAR_FORM()
    return render(request, 'DC_Finance/Add_fiscal_year.html', {'form': form})

def Add_department(request):
    if request.method == "POST":
        form = DEPARTMENT_FORM(request.POST)
        if form.is_valid():
            Department = form.save(commit=False)
            Department.save()
            return redirect('/fin/department',)
    else:
        form = DEPARTMENT_FORM()
    return render(request, 'DC_Finance/Add_department.html', {'form': form})

def Add_program(request):
    if request.method == "POST":
        form = Program_FORM(request.POST)
        if form.is_valid():
            Program = form.save(commit=False)
            Program.save()
            return redirect('/fin/program',)
    else:
        form = Program_FORM()
    return render(request, 'DC_Finance/Add_program.html', {'form': form})

def Add_faculty(request):
    if request.method == "POST":
        form = FACULTY_FORM(request.POST)
        if form.is_valid():
            FACULTY = form.save(commit=False)
            FACULTY.save()
            return redirect('/fin/faculty',)
    else:
        form = FACULTY_FORM()
    return render(request, 'DC_Finance/Add_faculty.html', {'form': form})

def Add_project(request):
    if request.method == "POST":
        form = Project_FORM(request.POST)
        if form.is_valid():
            Project = form.save(commit=False)
            Project.save()
            return redirect('/fin/project',)
    else:
        form = Project_FORM()
    return render(request, 'DC_Finance/Add_project.html', {'form': form})

def Add_funder(request):
    if request.method == "POST":
        form = FUNDER_FORM(request.POST)
        if form.is_valid():
            FUNDER = form.save(commit=False)
            FUNDER.save()
            return redirect('/fin/funder',)
    else:
        form = FUNDER_FORM()
    return render(request, 'DC_Finance/Add_funder.html', {'form': form})

def Add_naics_classification(request):
    if request.method == "POST":
        form = NAICS_CLASSIFICATION_FORM(request.POST)
        if form.is_valid():
            NAICS_CLASSIFICATION = form.save(commit=False)
            NAICS_CLASSIFICATION.save()
            return redirect('/fin/naics_classification',)
    else:
        form = NAICS_CLASSIFICATION_FORM()
    return render(request, 'DC_Finance/Add_naics_classification.html', {'form': form})

def Add_review(request):
    if request.method == "POST":
        form = REVIEW_FORM(request.POST)
        if form.is_valid():
            REVIEW = form.save(commit=False)
            REVIEW.save()
            return redirect('/fin/review',)
    else:
        form = REVIEW_FORM()
    return render(request, 'DC_Finance/Add_review.html', {'form': form})

def Add_finance(request):
    if request.method == "POST":
        form = FINANCE_FORM(request.POST)
        if form.is_valid():
            FINANCE = form.save(commit=False)
            FINANCE.save()
            return redirect('/fin/finance',)
    else:
        form = FINANCE_FORM()
    return render(request, 'DC_Finance/Add_finance.html', {'form': form})

def Add_student(request):
    if request.method == "POST":
        form = STUDENT_FORM(request.POST)
        if form.is_valid():
            STUDENT = form.save(commit=False)
            STUDENT.save()
            return redirect('/fin/student',)
    else:
        form = STUDENT_FORM()
    return render(request, 'DC_Finance/Add_student.html', {'form': form})

def Add_funding_level(request):
    if request.method == "POST":
        form = FUNDING_LEVEL_FORM(request.POST)
        if form.is_valid():
            FUNDING_LEVEL = form.save(commit=False)
            FUNDING_LEVEL.save()
            return redirect('/fin/funding_level',)
    else:
        form = FUNDING_LEVEL_FORM()
    return render(request, 'DC_Finance/Add_funding_level.html', {'form': form})

def Add_industry_size(request):
    if request.method == "POST":
        form = INDUSTRY_SIZE_FORM(request.POST)
        if form.is_valid():
            INDUSTRY_SIZE = form.save(commit=False)
            INDUSTRY_SIZE.save()
            return redirect('/fin/industry_size',)
    else:
        form = INDUSTRY_SIZE_FORM()
    return render(request, 'DC_Finance/Add_industry_size.html', {'form': form})


def Add_resource(request):
    faculty = FACULTY.objects.filter()
    student = STUDENT.objects.filter()


    form = RESOURCE_FORM(request.POST)
    if request.method == 'POST':
        print('add resource 1')
        if form.is_valid():
            RESOURCE = form.save(commit=False)
            RESOURCE.Resource_name = request.POST.get('Resource_name')
            RESOURCE.save()
            return redirect('/fin/resource',)
    else:
        print('add resource 2')
        form = RESOURCE_FORM()
    return render(request, 'DC_Finance/Add_resource.html', {'form': form,'faculty':faculty,'student':student})

def Faculty_dropdown_update(request):
    print('received request!')
    if request.method == 'GET':
        data = FACULTY.objects.values_list('Professor_Name', flat=True)
        data = json.dumps(list(data))
        print(data)
        return HttpResponse(data, content_type='application/json')
    else:
        print('wrong request to F-dropdown')

def Student_dropdown_update(request):
    print('received request!')
    if request.method == 'GET':
        data = STUDENT.objects.values_list('Student_Name', flat=True)
        data = json.dumps(list(data))
        print(data)
        return HttpResponse(data, content_type='application/json')
    else:
        print('wrong request to S-dropdown')
    
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.apps import apps
# Create your models here.

#creating choice list for dropdown
CHOICES = (('Yes','Yes'),('No', 'No'),('Nil', 'Nil'))
POSITION = (('Project Manager','Project Manager'), ('Principal Investigator','Principal Investigator'), ('Project Co-ordinator','Project Co-ordinator'), ('Research Assistant','Research Assistant'), ('Research Associate','Research Associate'))
Project_outcome_choices = (('Product','Product'),('Process','Process'),('Service','Service'),('Product/Prototype','Product/Prototype'),('Process/Prototype','Process/Prototype'),('Nil','Nil'))
Selection_resource = (('FACULTY','FACULTY'),('STUDENT','STUDENT'))

#Project partner table when used as foreign key returns project partner name
class PROJECT_PARTNER(models.Model):
    Project_Partner = models.CharField(max_length=20)
    Project_Partner_NAICS_Classification = models.ForeignKey('NAICS_CLASSIFICATION', on_delete=models.CASCADE)
    Project_Partner_Size = models.ForeignKey('INDUSTRY_SIZE', on_delete=models.CASCADE)

    def __str__(self):
        return self.Project_Partner

#Research centre table
class RESEARCH_CENTRE(models.Model):
    Research_Centre = models.CharField(max_length=20)

    def __str__(self):
        return self.Research_Centre

#Fiscal year table
class FISCAL_YEAR(models.Model):
    #Fiscal_Year = models.DateTimeField()
    Fiscal_Year = models.CharField(max_length=10)
    def __str__(self):
        return self.Fiscal_Year

#Department table
class DEPARTMENT(models.Model):
    Faculty_Department = models.CharField(max_length=30)

    def __str__(self):
        return self.Faculty_Department

#Program table
class Program(models.Model):
    Program = models.CharField(max_length=30)

    def __str__(self):
        return self.Program

#Faculty table returns professor name
class FACULTY(models.Model):
    Professor_Name = models.CharField(max_length=20)
    ID_Number = models.CharField(max_length=20)
    Faculty_Department = models.ForeignKey('Department', on_delete=models.CASCADE)
    Internship_Supervisor = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    External_Principal_Investigator = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    Research_Associate = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    External_Research_Assistant = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    Administration_Support_Staff = models.CharField(max_length=20)
    Post_Doc = models.CharField(max_length=20)
    Technician_Name = models.CharField(max_length=20)
    Contract_hours = models.IntegerField()

    def __str__(self):
        return self.Professor_Name

#Project table returns project number
class Project(models.Model):
    Project_Name = models.CharField(max_length=60)
    Project_number = models.CharField(max_length=15)
    Project_Manager = models.CharField(max_length=20)
    Count_as_Project = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    Fiscal_Year = models.ForeignKey('FISCAL_YEAR', on_delete=models.CASCADE)
    Start_this_Fiscal = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    Professor_Name = models.ForeignKey('FACULTY', on_delete=models.CASCADE)
    Project_Partner = models.ForeignKey('PROJECT_PARTNER', on_delete=models.CASCADE)
    Research_Centre = models.ForeignKey('RESEARCH_CENTRE', on_delete=models.CASCADE)
    Clean_tech = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    Project_NAICS_Classification = models.ForeignKey('NAICS_CLASSIFICATION', on_delete=models.CASCADE)

    def __str__(self):
        return self.Project_number


class FUNDER(models.Model):
    Funder = models.CharField(max_length=20)
    Funding_Level = models.ForeignKey('FUNDING_LEVEL', on_delete=models.CASCADE)
    Project_number = models.ForeignKey('Project', on_delete=models.CASCADE)

class NAICS_CLASSIFICATION(models.Model):
    NAICS_Classification = models.CharField(max_length=50)
    #Clean_tech = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    #Project_number = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.NAICS_Classification

class REVIEW(models.Model):
    Project_start_date = models.DateTimeField()
    Project_end_date = models.DateTimeField()
    Business_solution = models.CharField(max_length=20)
    Project_outcome = models.CharField(max_length=20, choices=Project_outcome_choices, null=True, blank=True)
    Success_Story_Produced = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    Project_number = models.ForeignKey('Project', on_delete=models.CASCADE)

class FINANCE(models.Model):
    Funding_for_projects_Admin = models.IntegerField()
    Approved_industry_Partner_cash_Contribution = models.IntegerField()
    Approved_industry_partner_In_Kind_contribution = models.IntegerField()
    Funding_org_Roll_up = models.CharField(max_length=20)
    Grant_Number = models.CharField(max_length=20)
    Project_number = models.ForeignKey('Project', on_delete=models.CASCADE)
    
class STUDENT(models.Model):
    Student_Name = models.CharField(max_length=20)
    Fiscal_Year = models.ForeignKey('FISCAL_YEAR', on_delete=models.CASCADE)
    Research_Centre = models.ForeignKey('RESEARCH_CENTRE', on_delete=models.CASCADE)
    International_Student = models.CharField(max_length=5, choices=CHOICES, null=True, blank=True)
    Student_Number = models.IntegerField()
    Program = models.ForeignKey('Program', on_delete=models.CASCADE)
    Contract_Hours = models.IntegerField()
    Project_number = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.Student_Name


class FUNDING_LEVEL(models.Model):
    Funding_Level = models.CharField(max_length=50)

    def __str__(self):
        return self.Funding_Level

class INDUSTRY_SIZE(models.Model):
    Size = models.CharField(max_length=50)

    def __str__(self):
        return self.Size

        
class RESOURCE(models.Model):
    Project_number = models.ForeignKey('Project', on_delete=models.CASCADE)
    Resource_position = models.CharField(max_length=30, choices=POSITION, null=True, blank=True)
    Resource_select = models.CharField(max_length=30, choices=Selection_resource, null=True, blank=True)
    Resource_name = models.CharField(max_length=30)

    #selective_field = forms.ModelChoiceField(queryset=ModelA.objects.all(), empty_label="(Nothing selected)")    ---->   selective dropdown from same model

from .models import CompanyInformation, ProjectTitle, CompanyCash, projectinfoPI, teamexperts, workPlan
from django.forms import ModelForm


class CompanyInformationForm(ModelForm):

    class Meta:
        model = CompanyInformation
        fields = '__all__'
        exclude = ('status','files','note',)

class ProjectInfoForm(ModelForm):
    class Meta:
        model = ProjectTitle
        fields = '__all__'
        exclude = ('companyName','status')

class CompanyCashForm(ModelForm):
    class Meta:
        model = CompanyCash
        fields = '__all__'
        exclude = ('project',)

class ProjectinfoPIform(ModelForm): 
    class Meta:
        model = projectinfoPI
        fields = '__all__'
        exclude = ('project',) 

class workPlanForm(ModelForm):
    class Meta:
        model = workPlan
        fields = '__all__'
        exclude = ('projectTitle',) 

class teamexpertsForm(ModelForm):
    class Meta:
        model = teamexperts
        fields = '__all__'
        exclude = ('projectTitle',) 


       
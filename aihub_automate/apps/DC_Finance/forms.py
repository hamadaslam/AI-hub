from django import forms
from .models import *

class RESEARCH_CENTRE_FORM(forms.ModelForm):

    class Meta:
        model = RESEARCH_CENTRE
        fields = '__all__'

class PROJECT_PARTNER_FORM(forms.ModelForm):

    class Meta:
        model = PROJECT_PARTNER
        fields = '__all__'

class FISCAL_YEAR_FORM(forms.ModelForm):

    class Meta:
        model = FISCAL_YEAR
        fields = '__all__'

class DEPARTMENT_FORM(forms.ModelForm):

    class Meta:
        model = DEPARTMENT
        fields = '__all__'

class Program_FORM(forms.ModelForm):

    class Meta:
        model = Program
        fields = '__all__'

class FACULTY_FORM(forms.ModelForm):

    class Meta:
        model = FACULTY
        fields = '__all__'

class Project_FORM(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

class FUNDER_FORM(forms.ModelForm):

    class Meta:
        model = FUNDER
        fields = '__all__'

class NAICS_CLASSIFICATION_FORM(forms.ModelForm):

    class Meta:
        model = NAICS_CLASSIFICATION
        fields = '__all__'

class REVIEW_FORM(forms.ModelForm):

    class Meta:
        model = REVIEW
        fields = '__all__'

class FINANCE_FORM(forms.ModelForm):

    class Meta:
        model = FINANCE
        fields = '__all__'

class STUDENT_FORM(forms.ModelForm):

    class Meta:
        model = STUDENT
        fields = '__all__'

class FUNDING_LEVEL_FORM(forms.ModelForm):

    class Meta:
        model = FUNDING_LEVEL
        fields = '__all__'

class INDUSTRY_SIZE_FORM(forms.ModelForm):

    class Meta:
        model = INDUSTRY_SIZE
        fields = '__all__'

class RESOURCE_FORM(forms.ModelForm):

    class Meta:
        model = RESOURCE
        fields = '__all__'
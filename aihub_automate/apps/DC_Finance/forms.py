from django import forms
from .models import RESEARCH_CENTRE

class RESEARCH_CENTRE_FORM(forms.ModelForm):

    class Meta:
        model = RESEARCH_CENTRE
        fields = '__all__'
from django.shortcuts import render
from django.utils import timezone
from .models import RESEARCH_CENTRE
from .forms import RESEARCH_CENTRE_FORM

# Create your views here.
def research_center(request):
    research_center = RESEARCH_CENTRE.objects.filter()
    return render(request, 'DC_Finance/research_center.html', {'research_center': research_center})

def Add_Research_centre(request):
    form = RESEARCH_CENTRE_FORM()
    return render(request, 'DC_Finance/post_edit.html', {'form': form})
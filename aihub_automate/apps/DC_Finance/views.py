from django.shortcuts import render, redirect
from django.utils import timezone
from .models import RESEARCH_CENTRE
from .forms import RESEARCH_CENTRE_FORM

# Create your views here.
def research_center(request):
    research_center = RESEARCH_CENTRE.objects.filter()
    return render(request, 'DC_Finance/research_center.html', {'research_center': research_center})

def Add_Research_Centre(request):
    if request.method == "POST":
        form = RESEARCH_CENTRE_FORM(request.POST)
        if form.is_valid():
            Research_Centre = form.save(commit=False)
            Research_Centre.save()
            return redirect('research_centre.html',)
    else:
        form = RESEARCH_CENTRE_FORM()
    return render(request, 'DC_Finance/Add_Research_Centre.html', {'form': form})
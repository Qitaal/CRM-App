from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Lead
from .forms import LeadForm

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request,'lead_list.html', context)

def lead_detail(request, id):
    lead = Lead.objects.get(id=id)
    context = {
        'lead': lead
    }
    return render(request, 'lead_detail.html', context)

def lead_create(request):
    form = LeadForm()

    if request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/leads')
    
    context = {
        'form': form
    }
    return render(request, 'lead_create.html', context)
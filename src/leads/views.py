import django
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic

from .models import Lead
from .forms import LeadForm, CustomUserCreationForm

'''
Using Class Based View can reduce our code. This class provide various kinds of View 
like Create, Update, Delete, etc. Import it from django.views.generic.
'''

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'

# def landing_page(request):
#     return render(request, 'landing.html')

class LeadListView(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads
#     }
#     return render(request,'lead_list.html', context)

class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"

# def lead_detail(request, id):
#     lead = Lead.objects.get(id=id)
#     context = {
#         'lead': lead
#     }
#     return render(request, 'lead_detail.html', context)

class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Go to the site to see the new lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com'],
        )
        return super(LeadCreateView, self).form_valid(form)

# def lead_create(request):
#     form = LeadForm()

#     if request.method == 'POST':
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
    
#     context = {
#         'form': form
#     }
#     return render(request, 'lead_create.html', context)

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    
# def lead_update(request, id):
#     lead = Lead.objects.get(id=id)
#     form = LeadForm(instance=lead)

#     if request.method == 'POST':
#         form = LeadForm(request.POST, instance=lead)

#         if form.is_valid():
#             form.save()
#             return redirect('/leads/{}'.format(id))
    
#     context = {
#         'form': form,
#         'lead': lead,
#     }
#     return render(request, 'lead_update.html', context)

class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')

# def lead_delete(request, id):
#     lead = Lead.objects.get(id=id)
#     lead.delete()
#     return redirect('/leads')
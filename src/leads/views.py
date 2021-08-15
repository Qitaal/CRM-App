import django
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic

from .models import Lead
from .forms import LeadForm, CustomUserCreationForm
from agents.mixins import OrganisorLoginRequiredMixin

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

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor and user.is_agent:
            queryset = Lead.objects.all()
        # initial queryset of leads for the entire organisation
        elif user.is_organisor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads
#     }
#     return render(request,'lead_list.html', context)

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"

# def lead_detail(request, id):
#     lead = Lead.objects.get(id=id)
#     context = {
#         'lead': lead
#     }
#     return render(request, 'lead_detail.html', context)

class LeadCreateView(OrganisorLoginRequiredMixin, generic.CreateView):
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

class LeadUpdateView(OrganisorLoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    context_object_name = "lead"
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Lead.objects.filter(organization=user.userprofile)
    
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

class LeadDeleteView(OrganisorLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_success_url(self):
        return reverse('leads:lead_list')

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Lead.objects.filter(organization=user.userprofile)

# def lead_delete(request, id):
#     lead = Lead.objects.get(id=id)
#     lead.delete()
#     return redirect('/leads')
import random

from django.core.mail import send_mail
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Agent
from .forms import AgentForm
from .mixins import OrganisorLoginRequiredMixin


class AgentListView(OrganisorLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganisorLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()

        Agent.objects.create(
            user = user,
            organization = self.request.user.userprofile
        )

        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on DJCRM. Please come login to start working.",
            from_email="admin@test.com",
            recipient_list=[user.email],
        )
        
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentUpdateView(OrganisorLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    context_object_name = 'agent'
    form_class = AgentForm

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent_list')


class AgentDeleteView(OrganisorLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent_list')

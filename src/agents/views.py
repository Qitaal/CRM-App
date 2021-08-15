from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Agent
from .forms import AgentForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    context_object_name = 'agent'
    form_class = AgentForm

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent_list')


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent_list')

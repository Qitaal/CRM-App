from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import fields
from leads.models import Agent

user = get_user_model()

class AgentForm(forms.ModelForm):
    class Meta:
        model = user
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
        )
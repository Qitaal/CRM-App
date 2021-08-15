from django.urls import path
from .views import (
    AgentDeleteView, 
    AgentDetailView, 
    AgentListView,
    AgentCreateView, 
    AgentUpdateView,
)

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent_list'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent_detail'),
    path('create/', AgentCreateView.as_view(), name='agent_create'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent_update'),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agent_delete'),
]
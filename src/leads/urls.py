from django.urls import path

from .views import (
    lead_list, 
    lead_detail, 
    lead_create,
    lead_update,
)

app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<int:id>/', lead_detail),
    path('create/', lead_create),
    path('<int:id>/update/', lead_update),
]
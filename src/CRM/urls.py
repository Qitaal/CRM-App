from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from leads.views import LandingPageView, SignupView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('admin/', admin.site.urls),
    path('agents/', include('agents.urls', namespace='agents')),
    path('leads/', include('leads.urls', namespace='leads')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
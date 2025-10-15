from django.urls import path
from . import views

urlpatterns = [
    path('company-reports/', views.company_reports, name='company-reports'),
]

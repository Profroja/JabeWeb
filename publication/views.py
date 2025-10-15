from django.shortcuts import render
from .models import CompanyReport

def company_reports(request):
    reports = CompanyReport.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'company-reports.html', context)
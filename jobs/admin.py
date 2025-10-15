from django.contrib import admin
from .models import JobVacancy, JobApplication

@admin.register(JobVacancy)
class JobVacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'location', 'is_active', 'created_at']
    list_filter = ['job_type', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'location']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'job', 'email', 'status', 'created_at']
    list_filter = ['status', 'job', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'job__title']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']

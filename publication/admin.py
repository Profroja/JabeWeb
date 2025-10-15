from django.contrib import admin
from .models import CompanyReport

@admin.register(CompanyReport)
class CompanyReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'document', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Report Information', {
            'fields': ('title', 'document')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_date', 'created_at']
    list_filter = ['publication_date', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('News Information', {
            'fields': ('title', 'header_image', 'description', 'publication_date')
        }),
        ('Additional Images', {
            'fields': ('image_1', 'image_2', 'image_3', 'image_4'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
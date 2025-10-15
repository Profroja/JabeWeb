from django.contrib import admin
from .models import ImageGallery, VideoGallery

@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'video', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Video Information', {
            'fields': ('title', 'video')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
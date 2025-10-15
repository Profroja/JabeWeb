from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Category, SubCategory, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name', 'category__name']
    list_per_page = 20

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        
        # If subcategory is selected, ensure it belongs to the selected category
        if subcategory and category:
            if subcategory.category != category:
                raise forms.ValidationError({
                    'subcategory': 'Selected subcategory does not belong to the selected category.'
                })
        
        return cleaned_data

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = [
        'product_name', 
        'brand', 
        'model', 
        'category', 
        'subcategory', 
        'product_type',
        'image_1_preview'
    ]
    list_filter = [
        'product_type', 
        'category', 
        'subcategory', 
        'brand'
    ]
    search_fields = [
        'product_name', 
        'brand__name', 
        'model', 
        'category__name', 
        'subcategory__name'
    ]
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('product_name', 'brand', 'model', 'product_type')
        }),
        ('Categories', {
            'fields': ('category', 'subcategory')
        }),
        ('Images', {
            'fields': ('image_1', 'image_2', 'image_3')
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Always allow all subcategories in the form - validation will be handled in clean()
        form.base_fields['subcategory'].queryset = SubCategory.objects.all()
            
        return form
    
    class Media:
        js = ('admin/js/product_admin.js',)
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get-subcategories/', self.get_subcategories, name='get_subcategories'),
        ]
        return custom_urls + urls
    
    def get_subcategories(self, request):
        category_id = request.GET.get('category_id')
        if category_id:
            subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
            return JsonResponse(list(subcategories), safe=False)
        return JsonResponse([], safe=False)
    
    def image_1_preview(self, obj):
        if obj.image_1:
            return f"✓ Image 1"
        return "✗ No Image"
    image_1_preview.short_description = "Image 1"

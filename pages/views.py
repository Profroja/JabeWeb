from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from products.models import Product, Category, SubCategory, Brand
from gallery.models import ImageGallery, VideoGallery
from news.models import News
from jobs.models import JobVacancy, JobApplication

# Create your views here.
def home(request):
    # Get products for the showcase
    products = Product.objects.all()[:8]  # Get first 8 products
    
    # Get latest 3 news articles for the news section
    latest_news = News.objects.all()[:3]
    
    context = {
        'products': products,
        'latest_news': latest_news,
    }
    return render(request, 'homepage.html', context)

def about_us(request):
    return render(request, 'about-us.html')

def products(request):
    # Static products page - no database needed
    context = {}
    return render(request, 'products.html', context)

def contact_us(request):
    return render(request, 'contact-us.html')

def news(request):
    # Get the latest news articles
    latest_news = News.objects.all()[:3]  # Get latest 3 news articles for sidebar
    
    # Check if a specific news article is requested
    news_id = request.GET.get('news_id')
    selected_news = None
    
    if news_id:
        try:
            selected_news = News.objects.get(id=news_id)
        except News.DoesNotExist:
            selected_news = None
    
    # If no specific news is selected, show the most recent one
    if not selected_news:
        selected_news = News.objects.first()
    
    context = {
        'latest_news': latest_news,
        'selected_news': selected_news,
    }
    return render(request, 'news.html', context)

def product_detail(request, product_id):
    # Get the product or return 404
    product = get_object_or_404(Product, id=product_id)
    
    # Get related products (same category)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:6]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product-detail.html', context)

def image_gallery(request):
    images = ImageGallery.objects.all()
    context = {
        'images': images
    }
    return render(request, 'image-gallery.html', context)

def video_gallery(request):
    videos = VideoGallery.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'video-gallery.html', context)

def job_vacancies(request):
    # Get all active job vacancies
    jobs = JobVacancy.objects.filter(is_active=True).order_by('-created_at')
    
    # Get selected job (from URL parameter or first job)
    selected_job_id = request.GET.get('job_id')
    if selected_job_id:
        try:
            selected_job = JobVacancy.objects.get(id=selected_job_id, is_active=True)
        except JobVacancy.DoesNotExist:
            selected_job = jobs.first()
    else:
        selected_job = jobs.first()
    
    if request.method == 'POST':
        # Handle job application form submission
        try:
            job_id = request.POST.get('job_id')
            job = JobVacancy.objects.get(id=job_id, is_active=True)
            
            # Create job application
            application = JobApplication.objects.create(
                job=job,
                first_name=request.POST.get('first_name'),
                middle_name=request.POST.get('middle_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                date_of_birth=request.POST.get('date_of_birth'),
                nationality=request.POST.get('nationality'),
                current_location=request.POST.get('current_location'),
                education=request.POST.get('education'),
                institution=request.POST.get('institution'),
                year_completion=int(request.POST.get('year_completion')),
                experience_years=int(request.POST.get('experience_years')),
                recent_employer=request.POST.get('recent_employer'),
                heavy_equipment_experience=request.POST.get('heavy_equipment_experience'),
                expected_salary=request.POST.get('expected_salary'),
                cv_file=request.FILES.get('cv'),
                cover_letter=request.POST.get('cover_letter', '')
            )
            
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job-vacancies')
            
        except Exception as e:
            messages.error(request, 'There was an error submitting your application. Please try again.')
            return redirect('job-vacancies')
    
    context = {
        'jobs': jobs,
        'selected_job': selected_job,
    }
    return render(request, 'job-vacancies.html', context)

def sitemap_xml(request):
    """Generate sitemap.xml for search engines"""
    current_date = timezone.now().strftime('%Y-%m-%d')
    
    sitemap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Homepage -->
  <url>
    <loc>https://jabeinvestment.co.tz/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- About Us Page -->
  <url>
    <loc>https://jabeinvestment.co.tz/about-us/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  
  <!-- Products Page -->
  <url>
    <loc>https://jabeinvestment.co.tz/products/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  
  <!-- News Page -->
  <url>
    <loc>https://jabeinvestment.co.tz/news/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Contact Us Page -->
  <url>
    <loc>https://jabeinvestment.co.tz/contact-us/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Company Reports Page -->
  <url>
    <loc>https://jabeinvestment.co.tz/company-reports/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  
  <!-- Job Vacancies Page -->
  <url>
    <loc>https://jabeinvestment.co.tz/job-vacancies/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <!-- Image Gallery Page -->
  
</urlset>'''
    
    return HttpResponse(sitemap_content, content_type='application/xml')

def robots_txt(request):
    """Generate robots.txt for search engines"""
    robots_content = '''User-agent: *
Allow: /

# Sitemap
Sitemap: https://jabeinvestment.co.tz/sitemap.xml

# Disallow admin area
Disallow: /admin/

# Disallow media files (optional - you can remove this if you want media files indexed)
Disallow: /media/'''
    
    return HttpResponse(robots_content, content_type='text/plain')

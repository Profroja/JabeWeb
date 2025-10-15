from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('products/', views.products, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product-detail'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('news-updates/', views.news, name='news'),
    path('image-gallery/', views.image_gallery, name='image-gallery'),
    path('video-gallery/', views.video_gallery, name='video-gallery'),
    path('job-vacancies/', views.job_vacancies, name='job-vacancies'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap'),
    path('robots.txt', views.robots_txt, name='robots'),
]

from django.db import models

class ImageGallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Image Gallery"
        verbose_name_plural = "Image Gallery"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class VideoGallery(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='gallery/videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Video Gallery"
        verbose_name_plural = "Video Gallery"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

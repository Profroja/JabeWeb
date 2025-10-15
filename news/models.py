from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    header_image = models.ImageField(upload_to='news/header/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    image_1 = models.ImageField(upload_to='news/images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='news/images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='news/images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='news/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"
        ordering = ['-publication_date', '-created_at']
    
    def __str__(self):
        return self.title or "Untitled News Article"

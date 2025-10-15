from django.db import models

class CompanyReport(models.Model):
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='publications/reports/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Company Report"
        verbose_name_plural = "Company Reports"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

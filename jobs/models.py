from django.db import models
from django.utils import timezone

class JobVacancy(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]
    
    title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_time')
    location = models.CharField(max_length=100, default='Dar es Salaam')
    description = models.TextField()
    requirements = models.TextField(help_text="Enter requirements separated by new lines")
    responsibilities = models.TextField(blank=True, null=True, help_text="Enter responsibilities separated by new lines")
    qualifications = models.TextField(blank=True, null=True, help_text="Enter qualifications separated by new lines")
    experience_required = models.CharField(max_length=100, blank=True, null=True)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Job Vacancy"
        verbose_name_plural = "Job Vacancies"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    current_location = models.TextField()
    education = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year_completion = models.IntegerField()
    experience_years = models.IntegerField()
    recent_employer = models.CharField(max_length=200)
    heavy_equipment_experience = models.CharField(max_length=200)
    expected_salary = models.CharField(max_length=100)
    cv_file = models.FileField(upload_to='job_applications/cv/')
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"

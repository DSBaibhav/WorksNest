from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends Django's built-in User model.
    Every user gets one Profile automatically.
    role = 'recruiter' or 'seeker'
    """
    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('seeker', 'Job Seeker'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True, help_text='Comma-separated skills')
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Company(models.Model):
    """
    Company profile tied to a Recruiter.
    """
    recruiter = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='company'
    )
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    founded = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Job(models.Model):
    """
    A job listing posted by a Recruiter.
    """
    TYPE_CHOICES = [
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),
    ]
    LEVEL_CHOICES = [
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
        ('lead', 'Lead / Manager'),
    ]

    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs', null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    skills_required = models.TextField(blank=True, help_text='Comma-separated')
    job_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='full-time')
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='mid')
    location = models.CharField(max_length=100)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} @ {self.company}"

    def get_salary_display(self):
        if self.salary_min and self.salary_max:
            return f"₹{self.salary_min:,} – ₹{self.salary_max:,}"
        elif self.salary_min:
            return f"₹{self.salary_min:,}+"
        return "Not disclosed"


class Application(models.Model):
    """
    A Job Seeker's application to a Job.
    """
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('reviewing', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to='app_resumes/', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('job', 'applicant')  # Can't apply twice to same job
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"


class SavedJob(models.Model):
    """
    Job Seeker bookmarks a job for later.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_jobs')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='saved_by')
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')
from django.contrib import admin
from .models import Profile, Company, Job, Application, SavedJob

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'job_type', 'level', 'is_active', 'created_at']
    list_filter = ['job_type', 'level', 'is_active']
    search_fields = ['title', 'description']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'applied_at']
    list_filter = ['status']

admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(SavedJob)

admin.site.site_header = "WorksNest Admin"
admin.site.site_title = "WorksNest"

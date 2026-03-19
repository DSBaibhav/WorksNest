from django.urls import path
from . import views

urlpatterns = [
    # ── Public ──────────────────────────────
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),

    # ── Auth ────────────────────────────────
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),

    # ── Shared ──────────────────────────────
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    # ── Recruiter ───────────────────────────
    path('recruiter/jobs/new/', views.job_create, name='job_create'),
    path('recruiter/jobs/<int:pk>/edit/', views.job_edit, name='job_edit'),
    path('recruiter/jobs/<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('recruiter/applications/<int:pk>/', views.view_applications, name='view_applications'),
    path('recruiter/application/<int:pk>/status/', views.update_status, name='update_status'),
    path('recruiter/company/', views.company_profile, name='company_profile'),

    # ── Job Seeker ───────────────────────────
    path('jobs/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('jobs/<int:pk>/save/', views.save_job, name='save_job'),
    path('seeker/applications/', views.my_applications, name='my_applications'),
    path('seeker/saved/', views.saved_jobs, name='saved_jobs'),
]
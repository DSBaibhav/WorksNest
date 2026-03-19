from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Company, Job, Application, SavedJob
from .forms import RegisterForm, ProfileForm, CompanyForm, JobForm, ApplicationForm
from .forms import (
    RegisterForm, ProfileForm, CompanyForm,
    JobForm, ApplicationForm
)


# ──────────────────────────────────────────────
# PUBLIC VIEWS
# ──────────────────────────────────────────────

def home(request):
    """Landing page with featured jobs and stats."""
    recent_jobs = Job.objects.filter(is_active=True)[:6]
    total_jobs = Job.objects.filter(is_active=True).count()
    total_companies = Company.objects.count()
    total_seekers = Profile.objects.filter(role='seeker').count()
    return render(request, 'core/home.html', {
        'recent_jobs': recent_jobs,
        'total_jobs': total_jobs,
        'total_companies': total_companies,
        'total_seekers': total_seekers,
    })


def job_list(request):
    """Browse & search all active jobs."""
    jobs = Job.objects.filter(is_active=True)
    query = request.GET.get('q', '')
    job_type = request.GET.get('type', '')
    location = request.GET.get('location', '')

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(skills_required__icontains=query)
        )
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'core/job_list.html', {
        'jobs': jobs,
        'query': query,
        'job_type': job_type,
        'location': location,
    })


def job_detail(request, pk):
    """Single job page with apply button."""
    job = get_object_or_404(Job, pk=pk)
    already_applied = False
    already_saved = False

    if request.user.is_authenticated:
        already_applied = Application.objects.filter(
            job=job, applicant=request.user
        ).exists()
        already_saved = SavedJob.objects.filter(
            user=request.user, job=job
        ).exists()

    return render(request, 'core/job_detail.html', {
        'job': job,
        'already_applied': already_applied,
        'already_saved': already_saved,
    })


# ──────────────────────────────────────────────
# AUTHENTICATION VIEWS
# ──────────────────────────────────────────────

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            Profile.objects.create(user=user, role=role)
            if role == 'recruiter':
                Company.objects.create(recruiter=user, name=f"{user.username}'s Company")
            login(request, user)
            messages.success(request, f'Welcome to WorksNest, {user.username}!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


# ──────────────────────────────────────────────
# SHARED VIEWS
# ──────────────────────────────────────────────

@login_required
def dashboard(request):
    """Smart dashboard — different content based on role."""
    profile = request.user.profile
    context = {'profile': profile}

    if profile.role == 'recruiter':
        jobs = Job.objects.filter(recruiter=request.user)
        total_apps = Application.objects.filter(job__recruiter=request.user).count()
        context.update({
            'jobs': jobs,
            'total_apps': total_apps,
            'active_jobs': jobs.filter(is_active=True).count(),
        })
    else:
        applications = Application.objects.filter(applicant=request.user)
        saved = SavedJob.objects.filter(user=request.user)
        context.update({
            'applications': applications,
            'saved_jobs': saved,
        })

    return render(request, 'core/dashboard.html', context)


@login_required
def profile_view(request):
    profile = request.user.profile
    skills = [s.strip() for s in profile.skills.split(',')] if profile.skills else []
    return render(request, 'core/profile.html', {
        'profile': profile,
        'skills': skills,
    })


@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Also update User first/last name
            request.user.first_name = request.POST.get('first_name', '')
            request.user.last_name = request.POST.get('last_name', '')
            request.user.email = request.POST.get('email', '')
            request.user.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/profile_edit.html', {'form': form})


# ──────────────────────────────────────────────
# RECRUITER VIEWS
# ──────────────────────────────────────────────

@login_required
def job_create(request):
    if request.user.profile.role != 'recruiter':
        messages.error(request, 'Only recruiters can post jobs.')
        return redirect('dashboard')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.company = request.user.company
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'core/job_form.html', {'form': form, 'action': 'Post'})


@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated!')
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'core/job_form.html', {'form': form, 'action': 'Update'})


@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted.')
        return redirect('dashboard')
    return render(request, 'core/job_confirm_delete.html', {'job': job})


@login_required
def view_applications(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    applications = Application.objects.filter(job=job)
    return render(request, 'core/applications.html', {
        'job': job,
        'applications': applications,
    })


@login_required
def update_status(request, pk):
    app = get_object_or_404(Application, pk=pk, job__recruiter=request.user)
    if request.method == 'POST':
        app.status = request.POST.get('status', app.status)
        app.save()
        messages.success(request, f'Status updated to {app.get_status_display()}')
    return redirect('view_applications', pk=app.job.pk)


@login_required
def company_profile(request):
    company = get_object_or_404(Company, recruiter=request.user)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company profile updated!')
            return redirect('dashboard')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'core/company_profile.html', {'form': form, 'company': company})


# ──────────────────────────────────────────────
# JOB SEEKER VIEWS
# ──────────────────────────────────────────────

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    if request.user.profile.role != 'seeker':
        messages.error(request, 'Only job seekers can apply.')
        return redirect('job_detail', pk=pk)

    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied to this job.')
        return redirect('job_detail', pk=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.applicant = request.user
            app.save()
            messages.success(request, f'Applied to {job.title}! Good luck!')
            return redirect('my_applications')
    else:
        form = ApplicationForm()
    return render(request, 'core/apply.html', {'form': form, 'job': job})


@login_required
def save_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    saved, created = SavedJob.objects.get_or_create(user=request.user, job=job)
    if not created:
        saved.delete()
        messages.info(request, 'Job removed from saved.')
    else:
        messages.success(request, 'Job saved!')
    return redirect('job_detail', pk=pk)


@login_required
def my_applications(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'core/my_applications.html', {'applications': applications})


@login_required
def saved_jobs(request):
    saved = SavedJob.objects.filter(user=request.user)
    return render(request, 'core/saved_jobs.html', {'saved_jobs': saved})
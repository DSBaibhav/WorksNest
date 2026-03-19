from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Company, Job, Application


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    role = forms.ChoiceField(choices=[
        ('seeker', 'I am a Job Seeker'),
        ('recruiter', 'I am a Recruiter / Employer'),
    ])

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role']


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ['bio', 'location', 'phone', 'profile_pic', 'resume', 'skills', 'linkedin', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['recruiter']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['recruiter', 'company', 'created_at', 'updated_at']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
            'requirements': forms.Textarea(attrs={'rows': 4}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume']
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Tell us why you are a great fit for this role...'
            }),
        }
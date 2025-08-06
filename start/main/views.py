from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import UserProfile, Project, ProjectCategory, Skill
from .forms import ContactForm
from django.conf import settings


def home(request):
    profile = UserProfile.objects.first()
    educations = profile.educations.all() if profile else []
    experiences = profile.experiences.all() if profile else []
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    skills = Skill.objects.all().order_by('name')

    form = ContactForm()  # just to render form on homepage

    context = {
        'user_profile': profile,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'project_categories': categories,
        'skills': skills,
        'form': form,
    }
    return render(request, 'home.html', context)


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            try:
                send_mail(
                    subject=f"Portfolio Contact: {contact.subject}",
                    message=f"From: {contact.name}\nEmail: {contact.email}\n\n{contact.message}",
                    from_email=settings.EMAIL_HOST_USER,  # Use the configured email
                    recipient_list=[settings.EMAIL_HOST_USER],  # Send to yourself
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Failed to send email: {e}")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    # Render home again with errors if form is invalid
    profile = UserProfile.objects.first()
    educations = profile.educations.all() if profile else []
    experiences = profile.experiences.all() if profile else []
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    skills = Skill.objects.all().order_by('name')

    context = {
        'user_profile': profile,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'project_categories': categories,
        'skills': skills,
        'form': form,
    }
    return render(request, 'home.html', context)

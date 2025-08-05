from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserProfile, Education, Experience, Project, ProjectCategory, Skill, ContactRequest
from .forms import ContactForm

def home(request):
    # Always fetch the first (or specific) profile
    profile = UserProfile.objects.first()
    educations = profile.educations.all() if profile else []
    experiences = profile.experiences.all() if profile else []

    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    skills = Skill.objects.all().order_by('name')  # Fetch all skills

    # Contact form handling
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email to you
            send_mail(
                subject=f"Portfolio Contact: {contact.subject}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                from_email=contact.email,
                recipient_list=['muhileshkumarwork@gmail.com'],  # <-- Replace with your email
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # Avoid duplicate form submissions
    else:
        form = ContactForm()

    context = {
        'user_profile': profile,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'project_categories': categories,
        'skills': skills,
        'form': form,  # Pass form to template
    }
    return render(request, 'home.html', context)

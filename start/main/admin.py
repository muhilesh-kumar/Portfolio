from django.contrib import admin
from .models import UserProfile, Education, Experience, ProjectCategory, Project, Skill

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(Skill)
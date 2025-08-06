from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import contact_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("contact/", contact_form, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
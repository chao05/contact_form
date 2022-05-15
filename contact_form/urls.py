from django.contrib import admin
from django.urls import path, include
from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('', views.contact_view)
]
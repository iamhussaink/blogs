from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('home/',views.home, name='home'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/success/', views.contact_success, name='contact_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

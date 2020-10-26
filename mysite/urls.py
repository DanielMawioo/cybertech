from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
]

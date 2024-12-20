"""
URL configuration for Portify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

from django.views.i18n import set_language
from django.urls import path, include
from django.contrib import admin
from .views import submit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Default home page
    path('home-slider/', views.home_slider, name='home_slider'),
    path('home-video/', views.home_video, name='home_video'),
    path('home-image/', views.home_image, name='home_image'),
    path('home-classic/', views.home_classic, name='home_classic'),
    path('about-us/', views.about_us, name='about-us'),
    path('about-me/', views.about_us, name='about-me'),
    path('about-us-classic/', views.about_us, name='about-us-classic'),
    path('about-me-classic/', views.about_us, name='about-me-classic'),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('single-work-1/', views.single_work_1, name='single-work-1'),
    path('single-work-2/', views.single_work_2, name='single-work-2'),

    path('home-slider/', views.home_slider, name='home_slider'),
    path('home-image/', views.home_image, name='home_image'),
    path('home-classic/', views.home_classic, name='home_classic'),
    # Contact URLs
    path('contact/', views.contact, name='contact'),
    path('contact-2/', views.contact_2, name='contact_2'),
    
    # Blog URLs
    path('blog/', views.blog, name='blog'),
    path('publication/', views.publication, name='publication'),

    # mail submit
    path('submit/',submit, name='submit'),

    # language
    path('set-language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('set-language/', include('django.conf.urls.i18n')),
)



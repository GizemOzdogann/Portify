from django.shortcuts import render
from django.conf import settings


def home_video(request):
    return render(request, 'home-video.html')

def home(request):
    return render(request, 'home.html')

def home_slider(request):
    return render(request, 'home-slider.html')

def home_image(request):
    return render(request, 'home-image.html')

def home_classic(request):
    return render(request, 'home-classic.html')


def about_us(request):
    return render(request, 'about-us.html')
def about_me(request):
    return render(request, 'about-me.html')


def portfolio(request):
    social_links = settings.SOCIAL_MEDIA_LINKS
    return render(request, 'portfolio.html',{'social_links': social_links})

def single_work_1(request):
    return render(request, 'single-work-1.html')

def single_work_2(request):
    return render(request, 'single-work-2.html')

# Contact views
def contact(request):
    return render(request, 'contact.html')

def contact_2(request):
    return render(request, 'contact-2.html')

# Blog views
def blog(request):
    return render(request, 'blog.html')

def publication(request):
    return render(request, 'publication.html')

# mail 
from django.http import JsonResponse
from .models import ContactMessage

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate input
        if not name or not email or not message:
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        # Save message to the database
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        print(f"Saved message: Name={name}, Email={email}, Message={message}")

        return JsonResponse({
            'message': 'Form submitted successfully!',
            'data': {
                'name': name,
                'email': email,
                'message': message
            }
        })
    
    return JsonResponse({'error': 'Invalid request method.'}, status=405)


from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'home.html')

def python(request):
    return render(request, 'python.html')

def java(request):
    return render(request, 'java.html')

def cpp(request):
    return render(request, 'cpp.html')

def webdev(request):
    return render(request, 'webdev.html')

def machinelearning(request):
    return render(request, 'machinelearning.html')

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = f"Thank you for reaching out to us. Your message has been recieved. We will reply shortly.\n\nRecieved from {name}<{email}>\nMessage:\n{form.cleaned_data['message']}"

            # Send email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.EMAIL_HOST_USER,  # Replace with your 'from' email
                [email],  # Replace with a list of recipient emails
                fail_silently=False,
            )
            return render(request, 'about.html', {'form': ContactForm(), 'name': name})


    else:
        form = ContactForm()

    return render(request, 'about.html', {'form': form})

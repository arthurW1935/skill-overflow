from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'home.html')

def python(request):
    return render(request, 'languages/python.html')

def java(request):
    return render(request, 'languages/java.html')

def cpp(request):
    return render(request, 'languages/cpp.html')

def html(request):
    return render(request, 'languages/html.html')

def css(request):
    return render(request, 'languages/css.html')

def javascript(request):
    return render(request, 'languages/javascript.html')

def c(request):
    return render(request, 'languages/c.html')

def csharp(request):
    return render(request, 'languages/csharp.html')

def webdev(request):
    return render(request, 'topics/webdev.html')

def datascience(request):
    return render(request, 'topics/datascience.html')

def machinelearning(request):
    return render(request, 'topics/machinelearning.html')

def appdev(request):
    return render(request, 'topics/appdev.html')

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = f"Thank you for reaching out to us. Your message has been recieved. We will reply shortly.\n\nRecieved from {name}<{email}>\nMessage:\n{form.cleaned_data['message']}"

            send_mail(
                f'Contact Form Submission from {name}',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.EMAIL_HOST_USER, 
                [email], 
                fail_silently=False,
            )
            return render(request, 'about.html', {'form': ContactForm(), 'name': name})


    else:
        form = ContactForm()

    return render(request, 'about.html', {'form': form})

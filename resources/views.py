from django.shortcuts import render
from .forms import ContactForm

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
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form submission (e.g., send email)
            # You can use Django's email sending capabilities here
            pass

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

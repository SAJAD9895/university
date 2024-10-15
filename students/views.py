from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import os

def load_content(request, page):
    # Define the base path for your templates
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Construct the path to the HTML files
    content_map = {
        'about': os.path.join(base_dir, 'students','templates', 'students','about.html'),
        'contact': os.path.join(base_dir,'students', 'templates','students' ,'contact.html'),
        'home': os.path.join(base_dir,'students', 'templates','students' ,'home.html'),
    }
    
    # Read the content of the requested file
    if page in content_map:
        with open(content_map[page], 'r') as file:
            content = file.read()
        return JsonResponse({'content': content})
    return JsonResponse({'content': 'Page not found'}, status=404)

def home(request):
    return render(request, 'students/landing.html')  # Assuming your main HTML file is named home.html


def index(request):
    return HttpResponse("Hello, students!")
# Home Page View
# def home(request):
#     return render(request, 'students/home.html')

def students_list(request):
    return render(request, 'students/students_list.html')

def landing(request):
    return render(request, 'students/landing.html')

def about(request):
    return render(request, 'students/about.html')

def contact(request):
    return render(request, 'students/contact.html')
# Create your views here.

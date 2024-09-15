from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blogs

# Home Page View
def index(request):
    context = {
        "posts": Blogs.objects.filter(status=Blogs.ACTIVE)
    }
    print(context['posts'])
    return render(request, 'index.html', context)

# About us page view
def about(request):
    return render(request, 'about.html')

# Services page view
def services(request):
    return render(request, 'services.html')

# Contact us page view
def contact(request):
    return render(request, 'contact.html')

# Robots.txt
def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")
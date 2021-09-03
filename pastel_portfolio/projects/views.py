from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "../templates/index.html")

def projects(request):
    return render(request, '../templates/Projects.html')

def project_detail(request):
    return render(request, '../templates/project-details.html')

def blog_detial(request):
    return render(request, '../templates/blog-details.html')

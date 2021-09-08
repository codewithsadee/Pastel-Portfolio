from django.shortcuts import render
from .models import Porjects, Blog

# Create your views here.


def index(request):
    index = Porjects.objects.all()
    context = {
        'index' : index
    }
    return render(request, "../templates/index.html")



def projects(request):
    index = Porjects.objects.all()
    return render(request, '../templates/Projects.html')



def project_detail(request):
    project = Porjects.objects.get(pk=pk)
    context = {
        'projects' : projects
    }
    return render(request, '../templates/project-details.html')



def blog_detial(request):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog' : blog
    }
    return render(request, '../templates/blog-details.html')

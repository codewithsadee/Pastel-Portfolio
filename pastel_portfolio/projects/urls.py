from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('project-detail/', views.project_detail, name="project-detail"),
    path('blog-detail/', views.blog_detial, name="blog-detail"),
]
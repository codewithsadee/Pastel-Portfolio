from django.urls import path
from projects import views


urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path("<int:pk>/", views.project_detail, name="project-detail"),
    path('<int:pk>/', views.blog_detial, name="blog-detail"),
]
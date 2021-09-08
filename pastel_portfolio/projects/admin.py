from django.contrib import admin
from .models import Porjects, Blog


class ProjectsAdmin(admin.ModelAdmin):
     pass
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Porjects, ProjectsAdmin)
admin.site.register(Blog, BlogAdmin)

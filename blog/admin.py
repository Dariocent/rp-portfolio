from django.contrib import admin
from blog.models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
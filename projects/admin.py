from django.contrib import admin
from projects.models import Project, Technology, Category
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','pk')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Category,CategoryAdmin)

from multiprocessing import context
from django.shortcuts import render
from projects.models import Project, Category
# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    context = {
        'projects': projects,
        'categories': categories
    }
    return render(request, 'project_index.html', context)

def project_detail(request,pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

# def project_detail_slug(request,slug):
#     project = Project.objects.get(slug=slug)
#     context = {
#         'project': project
#     }
#     return render(request, 'project_detail.html', context)
    
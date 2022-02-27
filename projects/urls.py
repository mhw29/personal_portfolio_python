from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    #path('<slug:slug>', views.project_detail_slug, name='project_detail_slug'), #slug
]
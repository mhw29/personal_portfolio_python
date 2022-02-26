from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("aws_connect", views.aws_connect, name="aws_connect" ),
    path("email_translation_service", views.email_translation_service, name='email_translation_service'),
]
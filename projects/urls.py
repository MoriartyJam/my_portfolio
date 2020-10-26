from django.contrib import admin
from .views import project_detail, project_index
from django.urls import path, include


urlpatterns = [
    path("", project_index, name="project_index"),
    path("<int:pk>/", project_detail, name="project_detail"),
]
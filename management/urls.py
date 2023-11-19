"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.index, name="index"),

    # Teacher Routes
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard/teacher/add", views.teacher_add, name="teacher_add"),
    path("dashboard/teacher/view", views.teacher_view, name="teacher_view"),
    path("dashboard/teacher/edit/<int:id>", views.teacher_edit, name="teacher_edit"),
    path("dashboard/teacher/delete/<int:id>", views.teacher_delete, name="teacher_delete"),
]

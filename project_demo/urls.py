"""project_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from masonry.views import PostDetailView, subCategoriesData, PageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-details/<pk>/', PostDetailView.as_view(), name="post-details"),
    path('page-view/', PageView.as_view(), name="page-view"),
    path("subCategoriesData/", subCategoriesData, name="subCategoriesData")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

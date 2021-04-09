"""lecgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from lecgram.views import (first_view, get_request_attributes, get_json_format,
get_excel_file, get_files
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', first_view),
    path('request-attributes/', get_request_attributes),
    path('excel-file/', get_excel_file),
    path('returnjson/', get_json_format),
    path('my_files/', get_files),
]

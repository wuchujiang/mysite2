"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('add_book/', views.add_book),
    path('add_book3/', views.add_book3),
    path('add_book4/', views.add_book4),
    path('add_book5/', views.add_book5),
    path('remove_authors/', views.remove_authors),
    path('query1/', views.query1),
    path('query2/', views.query2),
    path('query3/', views.query3),
    path('query4/', views.query4),
    path('query5/', views.query5),
    path('agg/', views.agg),
    path('agg2/', views.agg2),
    path('book/', views.Book.as_view()),
]

"""
URL configuration for app project.

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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('player/', views.player),
    path('contact/', views.contact),
    path('index/', views.index),
    path('course/', views.course),
    path('calculator/', views.calculator),
    path('marksheet/', views.marksheet),
    path('fruit/', views.fruit),
    path('evenodd/', views.evenodd),
    path('playerdetail/',views.playerdetail),
    # path('course/<int:courseid>',views.coursesDetails)  # Dynamic url  int
    # path('course/<str:courseid>', views.coursesDetails)  # Dynamic url str
    # path('course/<slug:courseid>', views.coursesDetails)  # Dynamic url  slug
    #path('course/<courseid>', views.coursesDetails)  # Dynamic url  NONE Type
]

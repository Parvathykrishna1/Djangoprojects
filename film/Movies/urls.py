"""
URL configuration for film project.

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
from django.urls import path, include

from Movies import views

app_name="Movies"

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.movieListview.as_view(),name="home"),

    # path('addfilm/',views.addfilm,name="addfilm"),
    path('addfilm/',views.createview.as_view(),name="addfilm"),

    # path('viewdetails/<int:p>',views.viewdetails,name='viewdetails'),
    path('viewdetails/<int:pk>',views.Moviedetailview.as_view(),name="viewdetails"),

    # path('deletemovie/<int:p>',views.deletemovie,name='deletemovie'),
    path('deletemovie/<int:pk>',views.deleteview.as_view(),name='deletemovie'),


    # path('editmovie/<int:p>',views.editmovie,name='editmovie'),
    path('editmovie/<int:pk>',views.updateview.as_view(),name='editmovie'),
]

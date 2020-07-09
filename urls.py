"""project29 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app29 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex, name="main"),
    path('add_course/',views.addcourse,name="add_course"),
    path('save_course/',views.savecourse,name="save_course"),
    path('views_course/',views.viewscourse,name="views_course"),
    path('add_student/',views.addstudent,name="add_student"),
    path('save_student/',views.savestudent,name="save_student"),
    path('view_student/',views.viewstudent,name="view_student")
]

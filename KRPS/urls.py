"""KRPS URL Configuration

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
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('cabinet/', views.cabinet, name ="cabinet"),
    path('cabinet/courses/<int:course_id>/', views.course, name ="course"),
	path('cabinet/schedule/', views.schedule, name ="schedule"),
	path('cabinet/students/', views.students, name ="students"),
    path('cabinet/students/<int:course_name>&<str:group_name>/', views.marks),
    path('admin/', admin.site.urls),
    path('cabinet/finalMark/', views.finalMark, name ="finalMark"),
    path('cabinet/finalMark/<int:course_id>&<str:group_name>&<str:kofMark>&<str:kofAttendance>/', views.finalMarkStudent),
    path('cabinet/students/google/<int:course_name>&<str:group_name>/', views.googleSheets),
]

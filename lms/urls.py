"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# author: amit ; for uploading files 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='login'),
    path('home/', views.home, name='homepage'),
    path('courseview/<course_id>', views.course_view, name='courseview'),
    path('postNotice/', views.postNotice),
    path('deleteNotice/<int:id_notice>', views.deleteNotice),
    path('updateNotice/<int:id_notice>', views.updateNotice),
    path('postAssignment/', views.postAssignment),
    path('deleteAssignment/<int:id_assignment>', views.deleteAssignment),
    path('sendStudentSubmission/<int:id_assignment>', views.sendStudentSubmission),
    path('postSubmission/', views.postSubmission),
]


# for uploading files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
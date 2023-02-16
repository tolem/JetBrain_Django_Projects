from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('schedule/main/', IndexMenu.as_view(), name='main'),
    path('schedule/course_details/<int:course_id>', CourseDetails.as_view(), name="details"),
    path('schedule/teacher_details/<int:tutor_id>', TutorDetails.as_view(), name="tutor"),
    path('schedule/add_course/', AddCourse.as_view(), name="add_course"),
    path("login/", Login.as_view(), name="login"),
    path("signup/", Signup.as_view(), name="signup"),
]
from django.urls import path
from .views import ResumeMenu, ResumeList

app_name = "resume"

urlpatterns = [
    path("", ResumeMenu.as_view()),
    path("resumes", ResumeList.as_view()),
]


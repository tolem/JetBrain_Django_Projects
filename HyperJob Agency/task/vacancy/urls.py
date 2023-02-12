from django.urls import path
from .views import VacancyMenu, VacancyList

app_name = "vacancy"

urlpatterns = [
    path("vacancies", VacancyList.as_view())
]

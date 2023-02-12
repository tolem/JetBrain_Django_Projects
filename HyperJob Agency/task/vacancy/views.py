from django.shortcuts import render
from django.views import View
from .models import Vacancy


# Create your views here.
class VacancyMenu(View):
    def get(self, request):
        # *args, **kwargs
        return render(request, "resume/menu.html")


class VacancyList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancy.html', context={'data': Vacancy.objects.all()})
from django.shortcuts import render
from django.views import View
from .models import Resume


# Create your views here.
class ResumeMenu(View):
    def get(self, request):
        # *args, **kwargs
        return render(request, "resume/menu.html")


class ResumeList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resume.html', context={'data': Resume.objects.all()})
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import JobForm
from resume.models import Resume
from vacancy.models import Vacancy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class Menu(View):

    def get(self, request, *args, **kwargs):
        # form = JobForm()
        # form.label = "Create vacancy"
        # context = {'data': form}
        # if request.user.is_staff:
        #     form.label = "Create resume"
        return render(request, "hyperjob/home.html")

class Signup(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context = {'data': form}
        return render(request, "hyperjob/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {'data': form}
        return render(request, 'hyperjob/login.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            return redirect('/home')


class PostManager(View):
    def get(self, request, *args, **kwargs):
        print(request.user.is_staff, "hello", request.user.username, kwargs['jobs'])
        if request.user.is_authenticated:
            if request.user.is_staff and kwargs['jobs'] == "vacancy":
                form = JobForm()
                form.label = f"Create {kwargs['jobs']}"
                context = {'data': form, 'site': kwargs['jobs']}
                return render(request, 'hyperjob/create.html', context)

            if kwargs['jobs'] == "resume" and not request.user.is_staff:
                form = JobForm()
                form.label = "Create resume"
                context = {'data': form, 'site': kwargs['jobs']}
                return render(request, 'hyperjob/create.html', context)
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=403)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff and kwargs['jobs'] == "vacancy":
                desc = request.POST
                vacancy = Vacancy(author=request.user, description=desc['description'])
                vacancy.save()
                return redirect('/home')

            if kwargs['jobs'] == "resume":
                desc = request.POST
                resume = Resume(author=request.user, description=desc['description'])
                resume.save()
                return redirect('/home')

            else:
                return HttpResponse(status=403)

        else:
            return HttpResponse(status=403)

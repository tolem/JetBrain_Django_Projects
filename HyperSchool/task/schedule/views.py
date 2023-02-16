from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.views.generic.detail import DetailView
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class IndexMenu(View):

    def get(self, request, **kwargs):
        content = request.GET
        query = content.get('q')
        course_count, courses = Course.objects.all().count(), Course.objects.all()
        form = SearchForm(request.GET)
        if query:
            context = {'course_count': courses.filter(title__contains=query).count(), 'courses': courses.filter(title__contains=query), 'form': form}
            return render(request, 'schedule/index.html', context)

        if query is None or query == "":
            context = {'course_count': course_count, 'courses': courses, 'form': form}
            return render(request, 'schedule/index.html', context)


class CourseDetails(View):
    def get(self, request, **kwargs):
        course_id = kwargs['course_id']
        course = Course.objects.get(pk=course_id)
        teacher = course.teacher.all()
        print(teacher)
        context = {'course': course, 'teachers': teacher}

        return render(request, 'schedule/course_info.html', context)


class TutorDetails(View):
    def get(self, request, **kwargs):
        course_id = kwargs['tutor_id']
        teacher = Teacher.objects.get(pk=course_id)
        context = {'teacher': teacher}
        return render(request, 'schedule/teacher_info.html', context)


class AddCourse(View):
    def get(self, request, **kwargs):
        form = StudentSignUpForm()
        context = {'form': form}
        return render(request, 'schedule/add_course.html', context)

    def post(self, request, **kwargs):
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_course')


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {'data': form}
        return render(request, 'schedule/login.html', context)


    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            return redirect('main')


class Signup(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context = {'data': form}
        return render(request, "schedule/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        context = {'data': form}
        if form.is_valid():
            form.save()
            return redirect('main')
        return redirect('signup')



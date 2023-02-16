from django import forms
from django.forms import ModelForm
from .models import *


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', required=False, max_length=32)


class StudentSignUpForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

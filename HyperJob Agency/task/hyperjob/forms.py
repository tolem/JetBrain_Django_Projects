from django import forms


class JobForm(forms.Form):
    description = forms.CharField()
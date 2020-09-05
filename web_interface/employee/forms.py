from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

#Change path to parent directory for aneasier acces to files
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

type_of_employment =  [
    ('juma de norma', 'Jumatate de norma'),
    ('norma intreaga', 'Norma intreaga'),
    ]


class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField()
    second_name = forms.CharField()
    date_hire = forms.DateField()
    data_fired = forms.DateField(required=False)
    type_of_employment = forms.CharField(required=False, label='Tip de anjajare', widget=forms.Select(choices=type_of_employment))
    total_cost = forms.IntegerField(required=False)
    net_income = forms.IntegerField(required=False)
    brut_income = forms.IntegerField(required=False)
    function = forms.CharField(required=False)
    sediu = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'second_name', 'date_hire', 'data_fired', 'type_of_employment', 'total_cost', 'net_income', 'brut_income', 'function', 'sediu']

class EmployeeUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField()
    second_name = forms.CharField()
    date_hire = forms.DateField()
    data_fired = forms.DateField(required=False)
    type_of_employment = forms.CharField(required=False, label='Tip de anjajare', widget=forms.Select(choices=type_of_employment))
    total_cost = forms.IntegerField(required=False)
    net_income = forms.IntegerField(required=False)
    brut_income = forms.IntegerField(required=False)
    function = forms.CharField(required=False)
    sediu = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'second_name', 'date_hire', 'data_fired', 'type_of_employment', 'total_cost', 'net_income', 'brut_income', 'function', 'sediu']
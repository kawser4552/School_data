from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import *

class StudentForn(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
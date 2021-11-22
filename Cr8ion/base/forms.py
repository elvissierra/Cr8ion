from django import forms
from .models import Print


class PrintForm(forms.ModelForm):
    class Meta:
        model = Print
        fields = ("title", "description", "stl", "cover")

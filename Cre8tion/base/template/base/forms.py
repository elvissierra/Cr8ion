from django import forms
from .models import Prints


class PrintsForm(forms.ModelForm):
    class Meta:
        models = Prints
        fields = ("filename", "user", "description", "stl", "cover")

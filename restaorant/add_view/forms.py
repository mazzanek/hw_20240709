from django import forms
from .models import add_view

class AddForm(forms.ModelForm):
    class Meta:
        model = add_view
        fields = ["rest_name", "rest_spec", "rest_address", "rest_website", "rest_phone"]
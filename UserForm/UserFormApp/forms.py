from django import forms
from .models import UserDetails

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        exclude = ['suffix','phone_number','title','joining_date']

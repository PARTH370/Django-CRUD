from django import forms
from .models import UserDetail

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = "__all__"
        exclude = ['suffix','phone_number','title','joining_date']

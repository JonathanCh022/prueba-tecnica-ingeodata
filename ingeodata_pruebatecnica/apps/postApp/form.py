from django import forms
from ingeodata_pruebatecnica.apps.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
from django import forms
from apps.postApp import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = "__all__"
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
        }

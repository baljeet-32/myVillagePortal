from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Notification, Complaints, Jobs, Userquery


class AddNotification(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }


class AddComplaints(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['title', 'category', 'descritrion',  'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'descritrion': forms.Textarea(attrs={'class': 'form-control'}),

        }


class AddJob(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'descritrion', 'no_of_opening',
                  'salary_desc', 'location', 'contact_details', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'descritrion': forms.Textarea(attrs={'class': 'form-control'}),
            'no_of_opening': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_desc': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_details': forms.TextInput(attrs={'class': 'form-control'}),
            # 'status': forms.CheckboxInput(attrs={'class': 'form-control'})

        }


class UserQuery(forms.ModelForm):
    class Meta:
        model = Userquery
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.Textarea(attrs={'class': 'form-control'})
        }

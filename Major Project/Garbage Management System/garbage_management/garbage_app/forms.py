from django import forms
from .models import Bin, BinType, CollectionSchedule, MaintenanceLog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BinForm(forms.ModelForm):
    class Meta:
        model = Bin
        fields = ['location', 'capacity', 'current_fill', 'bintype']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bin Location'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Capacity (in Liters)'}),
            'current_fill': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current Fill (in Liters)'}),
            'bintype': forms.Select(attrs={'class': 'form-control'}),
        }

class BinTypeForm(forms.ModelForm):
    class Meta:
        model = BinType
        fields = ['name', 'description']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
        }

class CollectionScheduleForm(forms.ModelForm):
    class Meta:
        model = CollectionSchedule
        fields = ['bin', 'collection_date', 'collected_amount']
        widgets = {
            'bin': forms.Select(attrs={'class': 'form-control'}),
            'collection_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'collected_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Collected Amount (in Liters)'}),
        }

class MaintenanceLogForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = ['bin', 'maintenance_date', 'description']
        widgets = {
            'bin': forms.Select(attrs={'class': 'form-control'}),
            'maintenance_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Maintenance Description', 'rows': 7}),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
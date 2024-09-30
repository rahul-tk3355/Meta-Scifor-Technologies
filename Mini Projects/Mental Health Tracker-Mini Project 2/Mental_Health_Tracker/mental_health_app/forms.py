from django import forms
from .models import MoodEntry, TherapySession
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5, 
                'placeholder': 'Enter your notes...',
            }),
        }

class TherapySessionForm(forms.ModelForm):
    class Meta:
        model = TherapySession
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={
                'placeholder': 'dd-mm-yyyy', 
                'class': 'form-control',
                'type': 'date'
            }),
            'type': forms.Select(attrs={  # Use Select widget for dropdown
                'class': 'form-control',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter your notes...',
            }),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MoodEntry, TherapySession, Resource
from .forms import MoodEntryForm, TherapySessionForm, RegistrationForm
from django.contrib.auth import login,logout as auth_logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

@login_required
def mood_entries(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('mood_entries')
    else:
        form = MoodEntryForm()
    
    entries = MoodEntry.objects.filter(user=request.user)
    return render(request, 'mood_entries.html', {'form': form, 'entries': entries})

@login_required
def therapy_sessions(request):
    if request.method == 'POST':
        form = TherapySessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('therapy_sessions')
    else:
        form = TherapySessionForm()
    
    sessions = TherapySession.objects.filter(user=request.user)
    return render(request, 'therapy_sessions.html', {'form': form, 'sessions': sessions})


def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return render(request, 'registration/logout.html')
        


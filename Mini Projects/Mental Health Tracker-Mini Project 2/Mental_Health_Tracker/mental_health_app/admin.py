from django.contrib import admin
from .models import MoodEntry, TherapySession, Resource

@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mood', 'notes')
    ordering = ('-date',)
    search_fields = ('mood', 'notes') # Search by mood and notes
    list_filter = ('mood', 'date')   

@admin.register(TherapySession)
class TherapySessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'type', 'notes')
    ordering = ('-date',)
    search_fields = ('type', 'notes')  # Search by type and notes
    list_filter = ('type', 'date')  

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'description')
    search_fields = ('title', 'description')

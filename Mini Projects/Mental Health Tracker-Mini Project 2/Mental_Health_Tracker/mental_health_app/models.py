from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.mood}"

class TherapySession(models.Model):
    SESSION_TYPES = [
    ('cbt', 'Cognitive Behavioral Therapy (CBT)'),
    ('dbt', 'Dialectical Behavior Therapy (DBT)'),
    ('mbct', 'Mindfulness-Based Cognitive Therapy (MBCT)'),
    ('act', 'Acceptance and Commitment Therapy (ACT)'),
    ('exposure', 'Exposure Therapy'),
    ('family', 'Family Therapy'),
    ('sfbf', 'Solution-Focused Brief Therapy (SFBT)'),
    ('art', 'Art Therapy'),
    ('tf_cbt', 'Trauma-Focused Cognitive Behavioral Therapy (TF-CBT)'),
    ('schema', 'Schema Therapy'),
]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=50, choices=SESSION_TYPES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.get_type_display()}"


class Resource(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

    


from django import forms
from .models import Bin, CollectionSchedule

class BinForm(forms.ModelForm):
    class Meta:
        model = Bin
        fields = '__all__'

        labels = {
            'capacity': 'Capacity (litres)',
            'current_fill': 'Current Fill (litres)',
        }

class CollectionForm(forms.ModelForm):
    class Meta:
        model = CollectionSchedule
        fields = '__all__'

        labels = {
            'collected_amount': 'Collected Amount (litres)',
        }

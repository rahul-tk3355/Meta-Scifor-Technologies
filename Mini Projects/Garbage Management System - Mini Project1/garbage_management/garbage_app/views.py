from django.shortcuts import render, redirect
from .models import Bin, CollectionSchedule
from .forms import BinForm, CollectionForm

def dashboard(request):
    bin_form = BinForm()
    collection_form = CollectionForm()
    warning_message = None

    if request.method == 'POST':
        if 'add_bin' in request.POST:
            bin_form = BinForm(request.POST)
            if bin_form.is_valid():
                new_bin = bin_form.save()
            
                if new_bin.current_fill / new_bin.capacity * 100 > 80:
                    warning_message = f"Warning: Bin at {new_bin.location} is at {new_bin.current_fill}/{new_bin.capacity} ({new_bin.current_fill / new_bin.capacity * 100:.2f}%) capacity."
                return redirect('dashboard')
        elif 'add_collection' in request.POST:
            collection_form = CollectionForm(request.POST)
            if collection_form.is_valid():
                collection_form.save()
                return redirect('dashboard')

    bins = Bin.objects.all()
    collections = CollectionSchedule.objects.all()
    
    context = {
        'bin_form': bin_form,
        'collection_form': collection_form,
        'bins': bins,
        'collections': collections,
        'warning_message': warning_message,
    }
    return render(request, 'dashboard.html', context)
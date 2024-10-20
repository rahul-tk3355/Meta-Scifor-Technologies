from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout as auth_logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bin, BinType, CollectionSchedule, MaintenanceLog
from .forms import BinForm, BinTypeForm, CollectionScheduleForm, MaintenanceLogForm, RegistrationForm
from django.utils.dateformat import DateFormat
from django.db.models import Count


# Home view
def home(request):
    return render(request, 'home.html')


# Bin views
class BinListView(LoginRequiredMixin, ListView):
    model = Bin
    template_name = 'bin_list.html'
    context_object_name = 'bins'

class BinDetailView(LoginRequiredMixin, DetailView):
    model = Bin
    template_name = 'bin_detail.html'
    context_object_name = 'bin'

class BinCreateView(LoginRequiredMixin, CreateView):
    model = Bin
    form_class = BinForm
    template_name = 'create_bin.html'
    success_url = '/bins/'

class BinUpdateView(LoginRequiredMixin, UpdateView):
    model = Bin
    form_class = BinForm
    template_name = 'update_bin.html'
    success_url = '/bins/'

class BinDeleteView(LoginRequiredMixin, DeleteView):
    model = Bin
    template_name = 'delete_bin.html'
    success_url = '/bins/'

# BinType views
class BinTypeListView(LoginRequiredMixin, ListView):
    model = BinType
    template_name = 'bin_type_list.html'
    context_object_name = 'bintypes'

class BinTypeCreateView(LoginRequiredMixin, CreateView):
    model = BinType
    form_class = BinTypeForm
    template_name = 'create_bin_type.html'
    success_url = '/bin-types/'

class BinTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = BinType
    form_class = BinTypeForm
    template_name = 'update_bin_type.html'
    success_url = '/bin-types/'

class BinTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = BinType
    template_name = 'delete_bin_type.html'
    success_url = '/bin-types/'

# CollectionSchedule views
class CollectionListView(LoginRequiredMixin, ListView):
    model = CollectionSchedule
    template_name = 'collection_list.html'
    context_object_name = 'collections'

class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = CollectionSchedule
    form_class = CollectionScheduleForm
    template_name = 'create_collection.html'
    success_url = '/collections/'

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = CollectionSchedule
    form_class = CollectionScheduleForm
    template_name = 'update_collection.html'
    success_url = '/collections/'

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    model = CollectionSchedule
    template_name = 'delete_collection.html'
    success_url = '/collections/'

# MaintenanceLog views
class MaintenanceLogListView(LoginRequiredMixin, ListView):
    model = MaintenanceLog
    template_name = 'maintenance_log_list.html'
    context_object_name = 'logs'

class MaintenanceLogCreateView(LoginRequiredMixin, CreateView):
    model = MaintenanceLog
    form_class = MaintenanceLogForm
    template_name = 'create_maintenance_log.html'
    success_url = '/maintenance-logs/'

class MaintenanceLogUpdateView(LoginRequiredMixin, UpdateView):
    model = MaintenanceLog
    form_class = MaintenanceLogForm
    template_name = 'update_maintenance_log.html'
    success_url = '/maintenance-logs/'

class MaintenanceLogDeleteView(LoginRequiredMixin, DeleteView):
    model = MaintenanceLog
    template_name = 'delete_maintenance_log.html'
    success_url = '/maintenance-logs/'

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
        auth_logout(request)
        return render(request, 'registration/logout.html')
   

def bin_chart(request):
    bins = Bin.objects.all()  
    return render(request, 'charts/bin_chart.html', {'bins': bins})


def collection_chart(request):
    # Fetch the collections data
    collections = CollectionSchedule.objects.all().order_by('collection_date')

    # Prepare data for the chart
    dates = [DateFormat(collection.collection_date).format('Y-m-d') for collection in collections]
    collected_amounts = [collection.collected_amount for collection in collections]

    context = {
        'dates': dates,  # Collection dates as labels
        'collected_amounts': collected_amounts,  # Collected amounts
    }

    return render(request, 'charts/collection_chart.html', context)

def maintenance_chart(request):
    logs = MaintenanceLog.objects.values('bin__location').annotate(count=Count('id')).order_by('bin__location')
    locations = [log['bin__location'] for log in logs]
    counts = [log['count'] for log in logs]

    return render(request, 'charts/maintenance_chart.html', {
        'locations': locations,
        'counts': counts,
    })
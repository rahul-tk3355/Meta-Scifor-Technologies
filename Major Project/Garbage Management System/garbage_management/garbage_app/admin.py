from django.contrib import admin
from .models import Bin, BinType, CollectionSchedule, MaintenanceLog

@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ('location', 'capacity', 'current_fill', 'bintype', 'fill_percentage')
    search_fields = ('location', 'bintype__name')

@admin.register(BinType)
class BinTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(CollectionSchedule)
class CollectionScheduleAdmin(admin.ModelAdmin):
    list_display = ('bin', 'collection_date', 'collected_amount')
    search_fields = ('bin__location',)
    list_filter = ('collection_date',)

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('bin', 'maintenance_date', 'description')
    search_fields = ('bin__location', 'description')
    list_filter = ('maintenance_date',)

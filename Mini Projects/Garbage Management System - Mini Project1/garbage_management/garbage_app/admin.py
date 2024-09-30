from django.contrib import admin
from .models import Bin, CollectionSchedule

class BinAdmin(admin.ModelAdmin):
    list_display = ('location', 'capacity', 'current_fill', 'fill_percentage')
    search_fields = ('location',)
    
class CollectionScheduleAdmin(admin.ModelAdmin):
    list_display = ('bin', 'collection_date', 'collected_amount')
    search_fields = ('bin__location',)

admin.site.register(Bin, BinAdmin)
admin.site.register(CollectionSchedule,CollectionScheduleAdmin )
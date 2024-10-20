from django.db import models
from django.utils import timezone

class BinType(models.Model):
    BIN_TYPE_CHOICES = [
        ('recyclable', 'Recyclable'),
        ('organic', 'Organic'),
        ('non_recyclable', 'Non-Recyclable'),
        ('e_waste', 'Electronic Waste'),
        ('hazardous', 'Hazardous Waste'),
        ('compost', 'Compost'),
        ('paper', 'Paper'),
        ('plastic', 'Plastic'),
        ('glass', 'Glass'),
        ('metal', 'Metal'),
        ('mixed', 'Mixed Waste'),
        ('bulky', 'Bulky Waste'),
        ('medical', 'Medical Waste'),
        ('construction', 'Construction Waste'),
        ('industrial', 'Industrial Waste'),
    ]
    name = models.CharField(max_length=100, choices=BIN_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Bin(models.Model):
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    current_fill = models.IntegerField()
    bintype = models.ForeignKey(BinType, on_delete=models.CASCADE)

    @property
    def fill_percentage(self):
        if self.capacity > 0:
            return (self.current_fill / self.capacity) * 100
        return 0

    def __str__(self):
        return f"{self.location} - {self.fill_percentage:.2f}%"

class CollectionSchedule(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    collection_date = models.DateTimeField(default=timezone.now)
    collected_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"Collection at {self.bin.location} on {self.collection_date}"

    class Meta:
        ordering = ['collection_date']

class MaintenanceLog(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    maintenance_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"Maintenance on {self.bin.location} at {self.maintenance_date}"

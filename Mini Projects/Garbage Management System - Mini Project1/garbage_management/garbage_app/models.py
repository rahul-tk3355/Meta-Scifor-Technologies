from django.db import models

class Bin(models.Model):
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    current_fill = models.IntegerField()

    @property
    def fill_percentage(self):
        return (self.current_fill / self.capacity) * 100

    def __str__(self):
        return f"{self.location} - {self.fill_percentage:.2f}%"
    

class CollectionSchedule(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    collection_date = models.DateTimeField()
    collected_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"Collection at {self.bin.location} on {self.collection_date}"
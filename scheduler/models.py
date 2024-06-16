from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class Day(models.Model):
    name = models.CharField(max_length=9, unique=True)  # 'Monday', 'Tuesday', etc.

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.title} on {self.day} at {self.time_slot}"

    class Meta:
        unique_together = ('day', 'time_slot', 'user')
        ordering = ['day', 'time_slot']

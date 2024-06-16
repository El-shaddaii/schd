from django.contrib import admin
from .models import Event, TimeSlot, Day

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'time_slot', 'user')
    search_fields = ('title', 'description', 'day__name', 'user__username')
    list_filter = ('day', 'time_slot', 'user')

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')
    list_filter = ('start_time', 'end_time')

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

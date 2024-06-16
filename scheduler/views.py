from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event, Day, TimeSlot

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page or list of events
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def index(request):
    days = Day.objects.all().order_by('id')  # Replace with your desired ordering
    time_slots = TimeSlot.objects.all().order_by('start_time')  # Replace with your desired ordering
    events = Event.objects.all()

    context = {
        'days': days,
        'time_slots': time_slots,
        'events': events,
    }
    return render(request, 'index.html', context)

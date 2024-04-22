from django.shortcuts import render
from django.http import HttpResponse

from .models import Person, PersonDetail, Event, EventDetail

# Create your views here.
def index(request):
    """The home page for History Gallery."""
    return render(request, 'galleries/index.html')


def persons(request):
    """Show all persons."""
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'galleries/persons.html', context)


def person_detail(request, person_id):
    """Show a single person's details."""
    person = Person.objects.get(id=person_id)

    person_details = person.persondetail_set.all()
    context = {'person': person, 'person_details': person_details}
    return render(request, 'galleries/person_detail.html', context)


def new_person(request):
    """Add a new person."""


def edit_person(request):
    """Edit an existing person."""


def events(request):
    """Show all events."""
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'galleries/events.html', context)


def event(request, event_id):
    """Show a single event's details."""
    event = Event.objects.get(id=event_id)

    event_details = event.eventdetail_set.all()
    context = {'event': event, 'event_details': event_details}
    return render(request, 'galleries/event_detail.html', context)


def new_event(request):
    """Add a new event."""


def edit_event(request):
    """Edit an existing event."""
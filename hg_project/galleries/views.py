from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """The home page for History Gallery."""
    return HttpResponse("Hello, world. You're at the galleries index.")


def persons(request):
    """Show all persons."""


def person(request):
    """Show a single person's details."""


def new_person(request):
    """Add a new person."""


def edit_person(request):
    """Edit an existing person."""


def events(request):
    """Show all events."""


def event(request):
    """Show a single event's details."""


def new_event(request):
    """Add a new event."""


def edit_event(request):
    """Edit an existing event."""
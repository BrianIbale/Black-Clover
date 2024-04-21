"""Defines URL patterns for galleries."""

from django.urls import path

from . import views

app_name = 'galleries'
urlpatterns = [
    # Home page
    path("", views.index, name="index"),

    # Page that shows all persons.
    path('persons/', views.persons, name='persons'),
    # Detail page for a single person.
    path('persons/<int:person_id>/', views.person_detail, name='person_detail'),
    # Page for adding a new person.
    path('new_person/', views.new_person, name='new_person'),
    # Page for editing a person.
    path('edit_person/<int:person_id>/', views.edit_person, name='edit_person'),
    
    # Page that shows all events.
    path('events', views.events, name='events'),
    # Detail page for a single event.
    path('events/<int:event_id>/', views.event, name='event'),
    # Page for adding a new event.
    path('new_event/', views.new_event, name='new_event'),
    # Page for editing a person.
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
]
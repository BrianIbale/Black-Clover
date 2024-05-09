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
    
    # Page that shows all events.
    path('events', views.events, name='events'),
    # Detail page for a single event.
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),

    # Page that shows all foods.
    path('foods', views.foods, name='foods'),
    # Detail page for a single event.
    path('foods/<int:food_id>/', views.food_detail, name='food_detail'),
]
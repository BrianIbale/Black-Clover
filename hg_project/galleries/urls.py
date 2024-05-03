"""Defines URL patterns for galleries."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'galleries'
urlpatterns = [
    # Home page
    path("", views.index, name="index"),

    # Page that shows all persons.
    path('persons/', views.persons, name='persons'),
    # Detail page for a single person.
    path('persons/<int:person_id>/<int:personimage_id>/', views.person_detail, name='person_detail'),
    
    # Page that shows all events.
    path('events', views.events, name='events'),
    # Detail page for a single event.
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
]

# Add the serving of media files URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
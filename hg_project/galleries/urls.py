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
    # Detail page for a single food.
    path('foods/<int:food_id>/', views.food_detail, name='food_detail'),
    
    # Page that shows all clothes.
    path('clothes', views.clothes, name='clothes'),
    # Detail page for a single clothe.
    path('clothes/<int:clothe_id>/', views.clothe_detail, name='clothe_detail'),

    # Page that shows all livelihoods.
    path('livelihoods', views.livelihoods, name='livelihoods'),
    # Detail page for a single livelihood.
    path('livelihoods/<int:livelihood_id>/', views.livelihood_detail, name='livelihood_detail'),
    
    # Page that shows all cultures.
    path('cultures', views.cultures, name='cultures'),
    # Detail page for a single culture.
    path('cultures/<int:culture_id>/', views.culture_detail, name='culture_detail'),

    # Page that shows all medicines.
    path('medicines', views.medicines, name='medicines'),
    # Detail page for a single medicine.
    path('medicines/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
]
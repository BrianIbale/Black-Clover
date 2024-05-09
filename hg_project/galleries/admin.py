from django.contrib import admin
from .models import Person, PersonDetail, PersonsImage, Event, EventDetail, EventImage

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonDetail)
admin.site.register(PersonsImage)
admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(EventImage)
from django.contrib import admin
from .models import Person, PersonDetail, Event, EventDetail, PersonImage

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonDetail)
admin.site.register(PersonImage)
admin.site.register(Event)
admin.site.register(EventDetail)
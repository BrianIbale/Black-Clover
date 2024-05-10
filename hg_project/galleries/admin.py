from django.contrib import admin
from .models import (Person, PersonDetail, PersonsImage, 
                     Event, EventDetail, EventImage, 
                     Food, FoodDetail, FoodImage, 
                     Clothe, ClotheDetail, ClotheImage, 
                     Livelihood, LivelihoodDetail, LivelihoodImage,
                     Culture, CultureDetail, CultureImage,
                     Medicine, MedicineDetail, MedicineImage)

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonDetail)
admin.site.register(PersonsImage)
admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(EventImage)
admin.site.register(Food)
admin.site.register(FoodDetail)
admin.site.register(FoodImage)
admin.site.register(Clothe)
admin.site.register(ClotheDetail)
admin.site.register(ClotheImage)
admin.site.register(Livelihood)
admin.site.register(LivelihoodDetail)
admin.site.register(LivelihoodImage)
admin.site.register(Culture)
admin.site.register(CultureDetail)
admin.site.register(CultureImage)
admin.site.register(Medicine)
admin.site.register(MedicineDetail)
admin.site.register(MedicineImage)
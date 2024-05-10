from django.shortcuts import render

from .models import (Person, PersonsImage, Event, EventImage,  Food, FoodImage, 
                     Clothe, ClotheImage, Livelihood, LivelihoodImage, 
                     Culture, CultureImage, Medicine, MedicineImage,
                     Invention, InventionImage)

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
    """Show a single person's details with images."""
    person = Person.objects.get(id=person_id)
    images = PersonsImage.objects.filter(person=person)

    person_details = person.persondetail_set.all()
    context = {'person': person, 'person_details': person_details, 'images': images}
    return render(request, 'galleries/person_detail.html', context)


def events(request):
    """Show all events."""
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'galleries/events.html', context)


def event_detail(request, event_id):
    """Show a single event's details with images."""
    event = Event.objects.get(id=event_id)
    images = EventImage.objects.filter(event=event)

    event_details = event.eventdetail_set.all()
    context = {'event': event, 'event_details': event_details, 'images': images}
    return render(request, 'galleries/event_detail.html', context)


def foods(request):
    """Show all foods."""
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'galleries/foods.html', context)


def food_detail(request, food_id):
    """Show a single food's details with images."""
    food = Food.objects.get(id=food_id)
    images = FoodImage.objects.filter(food=food)

    food_details = food.fooddetail_set.all()
    context = {'food': food, 'food_details': food_details, 'images': images}
    return render(request, 'galleries/food_detail.html', context)


def clothes(request):
    """Show all clothes."""
    clothes = Clothe.objects.all()
    context = {'clothes': clothes}
    return render(request, 'galleries/clothes.html', context)


def clothe_detail(request, clothe_id):
    """Show a single clothe's details with images."""
    clothe = Clothe.objects.get(id=clothe_id)
    images = ClotheImage.objects.filter(clothe=clothe)

    clothe_details = clothe.clothedetail_set.all()
    context = {'clothe': clothe, 'clothe_details': clothe_details, 'images': images}
    return render(request, 'galleries/clothe_detail.html', context)


def livelihoods(request):
    """Show all livelihoods."""
    livelihoods = Livelihood.objects.all()
    context = {'livelihoods': livelihoods}
    return render(request, 'galleries/livelihoods.html', context)


def livelihood_detail(request, livelihood_id):
    """Show a single livelihood's details with images."""
    livelihood = Livelihood.objects.get(id=livelihood_id)
    images = LivelihoodImage.objects.filter(livelihood=livelihood)

    livelihood_details = livelihood.livelihooddetail_set.all()
    context = {'livelihood': livelihood, 'livelihood_details': livelihood_details, 'images': images}
    return render(request, 'galleries/livelihood_detail.html', context)


def cultures(request):
    """Show all cultures."""
    cultures = Culture.objects.all()
    context = {'cultures': cultures}
    return render(request, 'galleries/cultures.html', context)


def culture_detail(request, culture_id):
    """Show a single culture's details with images."""
    culture = Culture.objects.get(id=culture_id)
    images = CultureImage.objects.filter(culture=culture)

    culture_details = culture.culturedetail_set.all()
    context = {'culture': culture, 'culture_details': culture_details, 'images': images}
    return render(request, 'galleries/culture_detail.html', context)


def medicines(request):
    """Show all medicines."""
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'galleries/medicines.html', context)


def medicine_detail(request, medicine_id):
    """Show a single medicine's details with images."""
    medicine = Medicine.objects.get(id=medicine_id)
    images = MedicineImage.objects.filter(medicine=medicine)

    medicine_details = medicine.medicinedetail_set.all()
    context = {'medicine': medicine, 'medicine_details': medicine_details, 'images': images}
    return render(request, 'galleries/medicine_detail.html', context)


def inventions(request):
    """Show all inventions."""
    inventions = Invention.objects.all()
    context = {'inventions': inventions}
    return render(request, 'galleries/inventions.html', context)


def invention_detail(request, invention_id):
    """Show a single invention's details with images."""
    invention = Invention.objects.get(id=invention_id)
    images = InventionImage.objects.filter(invention=invention)

    invention_details = invention.inventiondetail_set.all()
    context = {'invention': invention, 'invention_details': invention_details, 'images': images}
    return render(request, 'galleries/invention_detail.html', context)
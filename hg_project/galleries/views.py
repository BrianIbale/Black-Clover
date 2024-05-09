from django.shortcuts import render

from .models import Person, Event, EventImage, PersonsImage, Food, FoodImage, Clothe, ClotheImage

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
from django import forms

from .models import Person, Event

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['person_text']
        labels = {'person_text': ''}
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_text']
        labels = {'event_text': ''}
        widgets = {'event_text': forms.Textarea(attrs={'cols':80})}
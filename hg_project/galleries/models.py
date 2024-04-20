from django.db import models

# Create your models here.
class People(models.Model):
    people_text = models.CharField(max_length=200)

class Person(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    person_text = models.CharField(max_length=200)
    person_subtext = models.TextField()

class Events(models.Model):
    events_text = models.CharField(max_length=200)

class Event(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    event_text = models.CharField(max_length=200)
    event_subtext = models.TextField()
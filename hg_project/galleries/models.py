from django.db import models

# Create your models here.
class People(models.Model):
    people_text = models.CharField(max_length=200)

    def __str__(self):
        return self.people_text

class Person(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    person_text = models.CharField(max_length=200)
    person_subtext = models.TextField()

    def __str__(self):
        return self.person_subtext

class Events(models.Model):
    events_text = models.CharField(max_length=200)

    def __str__(self):
        return self.events_text

class Event(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    event_text = models.CharField(max_length=200)
    event_subtext = models.TextField()

    def __str__(self):
        return self.event_subtext
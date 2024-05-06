from django.db import models

# Create your models here.
class Person(models.Model):
    person_text = models.CharField(max_length=200)

    def __str__(self):
        return self.person_text


class PersonDetail(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person_subtext = models.TextField()

    def __str__(self):
        return f"{self.person_subtext[:50]}..."


class Event(models.Model):
    event_text = models.CharField(max_length=200)

    def __str__(self):
        return self.event_text


class EventDetail(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_subtext = models.TextField()

    def __str__(self):
        return self.event_subtext
    

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
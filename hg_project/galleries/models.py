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
    

class PersonImage(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Event(models.Model):
    event_text = models.CharField(max_length=200)

    def __str__(self):
        return self.event_text


class EventDetail(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_subtext = models.TextField()

    def __str__(self):
        return self.event_subtext
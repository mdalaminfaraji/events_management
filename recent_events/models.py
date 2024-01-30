from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')


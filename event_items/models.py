from django.db import models

class EventItems(models.Model):
    title = models.CharField(max_length=100)
    image = models.OneToOneField('EventItemImages', on_delete=models.CASCADE)

class EventItemImages(models.Model):
    image = models.ImageField(upload_to='event_items_images/')

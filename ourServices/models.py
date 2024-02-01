from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    features = models.JSONField(default=list)  # Store list of features as JSON
    servicesImage = models.ImageField(upload_to='services_images/')

    def __str__(self):
        return self.title


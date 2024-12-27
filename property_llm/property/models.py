from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Summary(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    summary = models.TextField()

class PropertyRating(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField()


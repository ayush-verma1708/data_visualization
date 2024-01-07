from django.db import models


# Create your models here.
class DataEntry(models.Model):
    intensity = models.FloatField()
    Likelihood = models.FloatField()
    Relevance = models.FloatField()
    Year = models.CharField(max_length = 255)
    Country= models.CharField(max_length = 255)
    Topics= models.CharField(max_length = 255)
    Region= models.CharField(max_length = 255)
    City = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.year}-{self.Country}-{self.City}'

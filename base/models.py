from django.db import models


# Create your models here.
class DataEntry(models.Model):
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.CharField(max_length = 255)
    country= models.CharField(max_length = 255)
    topics= models.CharField(null = True ,max_length = 255, default = "none")
    region= models.CharField(null = True ,max_length = 255)
    city = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.year}-{self.country}-{self.city}'
        
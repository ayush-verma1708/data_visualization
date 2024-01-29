from django.db import models
from django.utils import timezone

# Create your models here.
class DataEntry2(models.Model):
   from django.db import models

class DataEntry2(models.Model):
   end_year = models.IntegerField(blank=True, null=True, default=None)
   intensity = models.CharField(max_length=255,null=True, default=None)
   sector = models.CharField(max_length=255, blank=True, null=True, default=None)
   topic = models.CharField(max_length=255, blank=True, null=True, default=None)
   insight = models.CharField(max_length=255, null=True, default=None)
   url = models.URLField(blank=True, null=True, default=None)  
   region = models.CharField(max_length=255, blank=True, null=True, default=None)
   start_year = models.IntegerField(null=True, default=None)
   impact = models.CharField(max_length=255, blank=True, null=True, default=None)
   added = models.CharField(max_length=255,null=True, default=None)
   published = models.CharField(max_length=255,null=True, default=None)
   country = models.CharField(max_length=255, blank=True, null=True, default=None)
   relevance = models.CharField(max_length=255,null=True, default=None)
   pestle = models.CharField(max_length=255, blank=True, null=True, default=None)
   source = models.CharField(max_length=255, blank=True, null=True, default=None)
   title = models.CharField(max_length=255, null=True, default=None)
   likelihood = models.CharField(max_length=255,null=True, default=None)

   def __str__(self):
        return f'{self.start_year}-{self.country}'
    
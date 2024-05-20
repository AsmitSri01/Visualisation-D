from django.db import models


# Create your models here.
class Dashboard_data(models.Model):
    end_year = models.IntegerField(null=True, blank=True )
    intensity = models.FloatField(null=True)
    sector = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=50)
    start_year = models.IntegerField(null=True, blank=True)
    impact = models.TextField(blank=True)
    added = models.DateTimeField()
    published = models.DateTimeField(null=True)
    country = models.CharField(max_length=50)
    relevance = models.FloatField(null=True)
    pestle = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    likelihood = models.FloatField(null=True)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class Topic(models.Model): ## every model class has to inherit from 'models.Model'
    name = models.CharField(max_length=254, unique=True)

    def __str__(self): ## this function returns the attribute as a string
        return self.name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.date


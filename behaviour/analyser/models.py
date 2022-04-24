from django.db import models

class RawData(models.Model):
    title = models.CharField(max_length=200, default='mydata')
    media = models.FileField(
            null=True, 
            blank=True,
            upload_to='rawdata/'
            )

class Info(models.Model):
    preview = models.TextField()
    headers = models.TextField()
    ids = models.TextField()
    behaviors = models.TextField()
    categories = models.TextField()

class Interactions(models.Model):
    image = models.FileField(upload_to='interactions/')

class Transitions(models.Model):
    image = models.FileField(upload_to='transitions/')

class DataPlot(models.Model):
    image = models.ImageField(upload_to='data_plots/')
    
    
    





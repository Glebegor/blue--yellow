from django import forms
from django.db import models

class goodesCountFormModel(models.Model):
    FormCountCol = models.IntegerField()
    
    def __str__(self):
        return "firstCol"

class goodesModel(models.Model):
    Title = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    furniture = models.CharField(max_length=255)
    colors = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)
    imageGoodes = models.ImageField(upload_to="imagesGoodes")
    
    def __str__(self):
        return "{} {}".format(self.Title, self.version)
    def save(self, *args, **kwargs):
        self.Title = self.Title.lower()
        return super(goodesModel, self).save(*args, **kwargs)
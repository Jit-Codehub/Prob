from django.db import models

# Create your models here.
class Roman_Converter_Model(models.Model):
    inputEnter = models.CharField(max_length=250)
    detailStep = models.TextField()
    finalAnswer = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    solutionTitle = models.CharField(max_length=250)
    generateDate = models.DateField()
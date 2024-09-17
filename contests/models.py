from django.db import models

class Conform(models.Model):
    name = models.CharField(max_length=250)
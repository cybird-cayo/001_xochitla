from django.db import models

import os

class foto(models.Model):
    title = models.fields.DateTimeField()
    img = models.ImageField()
    id = models.BigAutoField(primary_key=True)

class letra(models.Model):
    title = models.fields.CharField(max_length=150)
    body = models.fields.TextField()
    id = models.BigAutoField(primary_key=True)




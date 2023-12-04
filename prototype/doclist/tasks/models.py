from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    
class Tasks(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete = models.CASCADE) # Si on supprime une collection, on_delete = models.CASCADE fait en sorte que les tâches associées à la collection le seront aussi
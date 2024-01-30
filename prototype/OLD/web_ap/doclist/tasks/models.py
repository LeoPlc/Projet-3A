from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    
    @classmethod
    def get_default_collection(cls) -> "Collection": # le -> "Collection" permet d'être sûr de faire comprendre à l'interpréteur que l'on a affaire à un objet de classe Collection
        collection, _ = cls.objects.get_or_create(name="Défaut",slug="_defaut")
        return collection
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete = models.CASCADE) # Si on supprime une collection, on_delete = models.CASCADE fait en sorte que les tâches associées à la collection le seront aussi
    def __str__(self):
        return self.description
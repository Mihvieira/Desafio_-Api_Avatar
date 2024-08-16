from django.db import models

class Personagem(models.Model):
           
    _id = models.CharField(max_length=255)
    allies = models.ManyToManyField("self") or []
    enemies = models.ManyToManyField("self") or []
    photoUrl = models.URLField(blank=True,)
    name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255) or ""
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Character(models.Model):
    character_image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    char_class = models.CharField(max_length=250)
    level = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=False)

def __str__(self):
    return self.name
    return self.species
    return self.char_class
    return self.level


from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=200, blank=True, null=True)
    img =models.CharField(max_length=200, blank=True, null=True)
    summary= models.TextField()

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    
   
    def __str__(self):
        return  (self.title)


class Watchlist(models.Model):
    
    watched= models.BooleanField()
    movie = models.ManyToManyField(
        Movies, related_name="movies")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userwatch")

    def __str__(self):
        return f"{self.user.username}: {self.movie}"
from django.db import models

# Create your models here.
class Actors(models.Model):
    actor_name = models.CharField(max_length=150,blank=False)


    def save_actor(self):
        self.save()

    @classmethod
    def get_category(cls):
        actor = Actors.objects.all()

        return actor

    def __str__(self):
        return self.actor_name

class Directors(models.Model):
    director_name = models.CharField(max_length=150,blank=False)


    def save_actor(self):
        self.save()

    @classmethod
    def get_category(cls):
        director = Directors.objects.all()

        return director

    def __str__(self):
        return self.director_name

class Movie(models.Model):
    movie_title = models.TextField(max_length=600)
    movie_year = models.IntegerField(blank=False)
    movie_length = models.IntegerField(blank=False)
    country = models.TextField(max_length=600)
    actor = models.ForeignKey(Actors,on_delete=models.CASCADE)
    director = models.ForeignKey(Directors,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_title

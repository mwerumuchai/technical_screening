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

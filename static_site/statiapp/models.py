from django.db import models


# Create your models here.
class place(models.Model):
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='spimage')
    disc = models.TextField()

    def __str__(self):
        return self.Name


class meet_team(models.Model):
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='mimage')
    disc = models.TextField()

    def __str__(self):
        return self.Name

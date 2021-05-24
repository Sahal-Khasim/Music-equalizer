from django.db import models


# Create your models here.
class Song(models.Model):

    title = models.CharField(max_length=100)
    song_file = models.FileField(upload_to="media",blank=True, null=True)




    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class DefaultSongs(models.Model):
    title= models.TextField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    paginate_by = 2

    def __str__(self):
        return self.title
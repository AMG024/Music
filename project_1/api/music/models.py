from django.db import models


# Create your models here.
class Music(models.Model):
    song = models.CharField( max_length = 256 ,null=True)
    poster = models.CharField( max_length = 256 ,null=True)
    singer = models.CharField( max_length = 100 ,null=True)
    Album  = models.CharField( max_length = 10 ,null=True)
    medium = models.CharField( max_length = 10 ,null=True)
    genre = models.CharField( max_length = 10 ,null=True)
    releasetime = models.CharField( max_length= 15 ,null=True)
    publisher= models.CharField( max_length= 15 ,null=True)
    mark = models.FloatField(null=True)


    class Meta:
        db_table = "music"

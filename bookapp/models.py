
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    author = models.CharField(db_column='author', max_length=100, blank=False)
    year = models.IntegerField(db_column='year', blank=False, default=2000)
    likes = models.IntegerField(db_column='likes', default=0)
    dislikes = models.IntegerField(db_column='dislikes', default=0)

    def __str__(self):
        return self.title   
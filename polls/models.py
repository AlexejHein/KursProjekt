from django.db import models


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField()


class Choice(models.Model):
    poll = models.ForeignKey(to='Poll', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

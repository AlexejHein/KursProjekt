from django.db import models


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    publish_time = models.DateTimeField()
    days_running = models.IntegerField(default=7)

    def __str__(self):
        return self.name + ' (' + self.slug + ')'


class Choice(models.Model):
    poll = models.ForeignKey(to='Poll', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}: {1}".format(self.poll.name, self.name)

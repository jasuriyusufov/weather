from django.db import models


class weatherInfo(models.Model):

    city = models.CharField(max_length=50)
    temperature = models.FloatField()
    humidity = models.IntegerField()

    def __str__(self):
        return f'{self.city}'

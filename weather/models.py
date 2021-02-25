from django.db import models


class City(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

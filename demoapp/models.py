from django.db import models

class serres(models.Model):
    no=models.CharField(max_length=4)
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
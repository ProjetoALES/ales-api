from django.db import models


class Semester(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    created = models.DateField(auto_now_add=True)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name

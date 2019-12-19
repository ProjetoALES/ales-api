from django.db import models
from login.models import User


class Professor(User):
    GENDERS = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]
    gender = models.CharField(max_length=1, choices=GENDERS)
    course = models.CharField(max_length=100)
    enroll_year = models.IntegerField()
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        self.is_professor = True
        super(Professor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ' - ' + self.email

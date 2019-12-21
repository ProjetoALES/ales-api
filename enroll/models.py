from django.db import models
from login.models import User


class Professor(User):
    course = models.CharField(max_length=100)
    enroll_year = models.IntegerField()

    def save(self, *args, **kwargs):
        self.is_professor = True
        super(Professor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ' - ' + self.email


class Student(User):
    document = models.CharField(max_length=20)
    authorization = models.BooleanField(default=False)
    address_code = models.CharField(max_length=20)
    LOCOMOTIONS = [
        ('BUS', 'Bus'),
        ('CAR', 'Car'),
        ('FOOT', 'Foot'),
        ('BIKE', 'Bike')
    ]
    locomotion = models.CharField(max_length=20, choices=LOCOMOTIONS)
    travel_time = models.TimeField()
    lunch_at_school = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_student = True
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ' - ' + self.email

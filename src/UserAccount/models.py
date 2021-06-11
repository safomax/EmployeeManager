from datetime import datetime

from django.db import models

# Create your models here.


class Employee(models.Model):

    employee_id = models.CharField(max_length=40, primary_key=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('None', 'Prefer not to say'))
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    employment_date = models.DateField()
    working_hours_from = models.TimeField(default=(datetime.now))
    working_hours_to = models.TimeField(default=(datetime.now))
    email = models.EmailField(max_length=255, unique=True, blank=True)
    primary_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    postalCode = models.CharField(max_length=40)
    primary_phone_number = models.CharField(max_length=10)
    other_phone_number = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField()
    salary = models.IntegerField( blank=True)
    STATUS_CHOICES = (('FT', 'Full_Time'), ('PT', 'Part_Time'), ('Temp', 'Temporary'), ('S', 'Seasonal'),)
    status = models.CharField(max_length=29, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'employee'


class Office(models.Model):
    office_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    postalCode = models.CharField(max_length=40)


class Position(models.Model):
    position = models.CharField(max_length=255)


class Team(models.Model):
    team = models.CharField(max_length=255)









from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(max_length=40, primary_key=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    employment_date = models.CharField(max_length=8)
    working_hours = models.CharField(max_length=8)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    primary_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    postalCode = models.CharField(max_length=40)
    primary_phone_number = models.CharField(max_length=10)
    other_phone_number = models.CharField(max_length=10, blank=True)
    date_of_birth = models.CharField(max_length=8)
    salary = models.IntegerField(max_length=8)
    status = models.CharField(max_length=12)


class Office(models.Model):
    office_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    postalCode = models.CharField(max_length=40)


class Position(models.Model):
    position = models.CharField(max_length=24)


class Team(models.Model):
    team = models.CharField(max_length=24)









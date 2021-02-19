from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=200)
    hospital_city = models.CharField(max_length=100)
    admin = models.CharField(max_length=200)
    def __str__(self):
        return self.hospital_name
    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})
    

class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_age = models.PositiveIntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name = 'patients_in_this_hospital')
    def __str__(self):
        return self.patient_name
    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.hospital.pk})


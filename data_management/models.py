from django.db import models

class Process(models.Model):
    process_name = models.CharField(max_length=128)

class Meas(models.Model):
    meas_type = models.CharField(max_length=128)
    course = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='modules')
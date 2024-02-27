# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class AluminumEtch(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    alum_etch_temp = models.CharField(max_length=400, blank=True, null=True)
    alum_etch_time = models.CharField(max_length=400, blank=True, null=True)
    stir_rpm = models.CharField(max_length=400, blank=True, null=True)
    metric_alum_etch_depth = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_photoresist_peeling = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_aluminum_peeling = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.


class AluminumEvaporation(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    aluminum_evaporation_temp = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    aluminum_evaporation_time = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    pressure_before_start_seq = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    pressure_before_evaporation = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_layer_thickness = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_layer_thick_qcm = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_deposition_rate = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class ChipList(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
class DepositionTemplate(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    glass_type = models.CharField(max_length=400, blank=True, null=True)
    cleaning_step = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    days_glass_at_room_temp = models.CharField(max_length=400, blank=True, null=True)
    prebake_temp = models.CharField(max_length=400, blank=True, null=True)
    prebake_time = models.CharField(max_length=400, blank=True, null=True)
    amount_drops = models.CharField(max_length=400, blank=True, null=True)
    spin_rpm = models.CharField(max_length=400, blank=True, null=True)
    spin_time = models.CharField(max_length=400, blank=True, null=True)
    bake_temp = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    bake_time = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    humidity = models.CharField(max_length=400, blank=True, null=True)
    metric_layer_thickness = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_cracking = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_particles = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class OxideEtch(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    max_temp_glass_reached = models.CharField(max_length=400, blank=True, null=True)
    oxide_etch_time = models.CharField(max_length=400, blank=True, null=True)
    oxide_etch_temp = models.CharField(max_length=400, blank=True, null=True)
    metric_oxide_etch_depth = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class Patterning(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    underlying_material = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    hdms_prebake_temp = models.CharField(max_length=400, blank=True, null=True)
    hdms_prebake_time = models.CharField(max_length=400, blank=True, null=True)
    hdms_spin_rpm = models.CharField(max_length=400, blank=True, null=True)
    hdms_spin_time = models.CharField(max_length=400, blank=True, null=True)
    hdms_bake_temp = models.CharField(max_length=400, blank=True, null=True)
    hdms_bake_time = models.CharField(max_length=400, blank=True, null=True)
    photoresist_spin_rpm = models.CharField(max_length=400, blank=True, null=True)
    photoresist_spin_time = models.CharField(max_length=400, blank=True, null=True)
    photoresist_bake_temp = models.CharField(max_length=400, blank=True, null=True)
    photoresist_bake_time = models.CharField(max_length=400, blank=True, null=True)
    exposure_pattern = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    exposure_time = models.CharField(max_length=400, blank=True, null=True)
    develop_time = models.CharField(max_length=400, blank=True, null=True)
    metric_pattern_quality = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_leftover_photoresist = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_missing_photoresist = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metric_contaminants = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.


class PlasmaClean(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    o2_flow = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    rf_power = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    clean_time = models.CharField(max_length=400, blank=True, null=True)
    metric_contaminants = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.


class PlasmaEtch(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    o2_flow = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    sf6_flow = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    rf_power = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    etch_time = models.CharField(max_length=400, blank=True, null=True)
    etch_depth = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
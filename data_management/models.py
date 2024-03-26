# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class ChipList(models.Model):
    chip_number = models.IntegerField(primary_key=True, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    IVCurrrents_CSV = models.FileField(blank=True)
    IVVoltages_CSV = models.FileField(blank=True)

class ChipListSearch(models.Model):
    chip_number = models.IntegerField(blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    creation_time = models.DateTimeField(blank=True)
    notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class AluminumEtch(models.Model):
    chip_number = models.ForeignKey(ChipList, on_delete=models.PROTECT, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    AluminumEtch_step_time = models.DateTimeField(blank=True)
    AluminumEtch_temp = models.CharField(max_length=400, blank=True, null=True)
    AluminumEtch_time = models.CharField(max_length=400, blank=True, null=True)
    AluminumEtch_stir_rpm = models.CharField(max_length=400, blank=True, null=True)
    AluminumEtch_metric_alum_etch_depth = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEtch_metric_photoresist_peeling = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEtch_metric_aluminum_peeling = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEtch_metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEtch_notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class AluminumEvaporation(models.Model):
    chip_number = models.ForeignKey(ChipList, on_delete=models.PROTECT, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    AluminumEvaporation_step_time = models.DateTimeField(blank=True)
    AluminumEvaporation_temp = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_time = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_pressure_before_start_seq = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_pressure_before_evaporation = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_metric_layer_thickness = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_metric_layer_thick_qcm = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_metric_deposition_rate = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    AluminumEvaporation_notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class Deposition(models.Model):
    chip_number = models.ForeignKey(ChipList, on_delete=models.PROTECT, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    Deposition_step_time = models.DateTimeField(blank=True)
    Deposition_glass_type = models.CharField(max_length=400, blank=True, null=True)
    Deposition_cleaning_step = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Deposition_days_glass_at_room_temp = models.CharField(max_length=400, blank=True, null=True)
    Deposition_prebake_temp = models.CharField(max_length=400, blank=True, null=True)
    Deposition_prebake_time = models.CharField(max_length=400, blank=True, null=True)
    Deposition_amount_drops = models.CharField(max_length=400, blank=True, null=True)
    Deposition_spin_rpm = models.CharField(max_length=400, blank=True, null=True)
    Deposition_spin_time = models.CharField(max_length=400, blank=True, null=True)
    Deposition_bake_temp = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Deposition_bake_time = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Deposition_humidity = models.CharField(max_length=400, blank=True, null=True)
    Deposition_metric_layer_thickness = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Deposition_metric_cracking = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Deposition_metric_particles = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Deposition_metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Deposition_notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class OxideEtch(models.Model):
    chip_number = models.ForeignKey(ChipList, on_delete=models.PROTECT, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    OxideEtch_step_time = models.DateTimeField(blank=True)
    OxideEtch_max_temp_glass_reached = models.CharField(max_length=400, blank=True, null=True)
    OxideEtch_time = models.CharField(max_length=400, blank=True, null=True)
    OxideEtch_temp = models.CharField(max_length=400, blank=True, null=True)
    OxideEtch_metric_oxide_etch_depth = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    OxideEtch_metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    OxideEtch_notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class Patterning(models.Model):
    chip_number = models.ForeignKey(ChipList, on_delete=models.PROTECT, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    Patterning_step_time = models.DateTimeField(blank=True)
    Patterning_underlying_material = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Patterning_hdms_prebake_temp = models.CharField(max_length=400, blank=True, null=True)
    Patterning_hdms_prebake_time = models.CharField(max_length=400, blank=True, null=True)
    Patterning_hdms_spin_rpm = models.CharField(max_length=400, blank=True, null=True)
    Patterning_hdms_spin_time = models.CharField(max_length=400, blank=True, null=True)
    Patterning_hdms_bake_temp = models.CharField(max_length=400, blank=True, null=True)
    Patterning_hdms_bake_time = models.CharField(max_length=400, blank=True, null=True)
    Patterning_photoresist_spin_rpm = models.CharField(max_length=400, blank=True, null=True)
    Patterning_photoresist_spin_time = models.CharField(max_length=400, blank=True, null=True)
    Patterning_photoresist_bake_temp = models.CharField(max_length=400, blank=True, null=True)
    Patterning_photoresist_bake_time = models.CharField(max_length=400, blank=True, null=True)
    Patterning_exposure_pattern = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Patterning_exposure_time = models.CharField(max_length=400, blank=True, null=True)
    Patterning_develop_time = models.CharField(max_length=400, blank=True, null=True)
    Patterning_metric_pattern_quality = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Patterning_metric_leftover_photoresist = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Patterning_metric_missing_photoresist = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Patterning_metric_contaminants = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Patterning_metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    Patterning_notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class PlasmaClean(models.Model):
    chip_number = models.ForeignKey(ChipList, on_delete=models.PROTECT, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    PlasmaClean_step_time = models.DateTimeField(blank=True)
    PlasmaClean_o2_flow = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaClean_rf_power = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaClean_clean_time = models.CharField(max_length=400, blank=True, null=True)
    PlasmaClean_metric_contaminants = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaClean_metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaClean_notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.

class PlasmaEtch(models.Model):
    chip_number = models.ForeignKey(ChipList, on_delete=models.PROTECT, blank=True)
    chip_owner    = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50)
    PlasmaEtch_step_time = models.DateTimeField(blank=True)
    PlasmaEtch_o2_flow = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaEtch_sf6_flow = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaEtch_rf_power = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaEtch_etch_time = models.CharField(max_length=400, blank=True, null=True)
    PlasmaEtch_etch_depth = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaEtch_metrology_link = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
    PlasmaEtch_notes = models.CharField(max_length=400, blank=True, null=True)  # This field type is a guess.
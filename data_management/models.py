# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AluminumEtch(models.Model):
    id = models.IntegerField()
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    alum_etch_temp = models.IntegerField(blank=True, null=True)
    alum_etch_time = models.IntegerField(blank=True, null=True)
    stir_rpm = models.IntegerField(blank=True, null=True)
    metric_alum_etch_depth = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_photoresist_peeling = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_aluminum_peeling = models.TextField(blank=True, null=True)  # This field type is a guess.
    metrology_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aluminum_etch'


class AluminumEvaporation(models.Model):
    id = models.IntegerField()
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    aluminum_evaporation_temp = models.TextField(blank=True, null=True)  # This field type is a guess.
    aluminum_evaporation_time = models.TextField(blank=True, null=True)  # This field type is a guess.
    pressure_before_start_seq = models.TextField(blank=True, null=True)  # This field type is a guess.
    pressure_before_evaporation = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_layer_thickness = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_layer_thick_qcm = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_deposition_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    metrology_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aluminum_evaporation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ChipList(models.Model):
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'chip_list'


class DataManagementCourse(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'data_management_course'


class DataManagementModule(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(DataManagementCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_management_module'


class DepositionTemplate(models.Model):
    id = models.IntegerField()
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    cleaning_step = models.TextField(blank=True, null=True)  # This field type is a guess.
    days_p504_at_room_temp = models.IntegerField(blank=True, null=True)
    prebake_temp = models.IntegerField(blank=True, null=True)
    prebake_time = models.IntegerField(blank=True, null=True)
    amount_drops = models.IntegerField(blank=True, null=True)
    spin_rpm = models.IntegerField(blank=True, null=True)
    spin_time = models.IntegerField(blank=True, null=True)
    bake_temp = models.TextField(blank=True, null=True)  # This field type is a guess.
    bake_time = models.TextField(blank=True, null=True)  # This field type is a guess.
    humidity = models.IntegerField(blank=True, null=True)
    metric_layer_thickness = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_cracking = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_particles = models.TextField(blank=True, null=True)  # This field type is a guess.
    metrology_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'deposition_template'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OxideEtch(models.Model):
    id = models.IntegerField()
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    max_temp_glass_reached = models.IntegerField(blank=True, null=True)
    oxide_etch_time = models.IntegerField(blank=True, null=True)
    oxide_etch_temp = models.IntegerField(blank=True, null=True)
    metric_oxide_etch_depth = models.TextField(blank=True, null=True)  # This field type is a guess.
    metrology_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'oxide_etch'


class Patterning(models.Model):
    id = models.IntegerField()
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    underlying_material = models.TextField(blank=True, null=True)  # This field type is a guess.
    hdms_prebake_temp = models.IntegerField(blank=True, null=True)
    hdms_prebake_time = models.IntegerField(blank=True, null=True)
    hdms_spin_rpm = models.IntegerField(blank=True, null=True)
    hdms_spin_time = models.IntegerField(blank=True, null=True)
    hdms_bake_temp = models.IntegerField(blank=True, null=True)
    hdms_bake_time = models.IntegerField(blank=True, null=True)
    photoresist_spin_rpm = models.IntegerField(blank=True, null=True)
    photoresist_spin_time = models.IntegerField(blank=True, null=True)
    photoresist_bake_temp = models.IntegerField(blank=True, null=True)
    photoresist_bake_time = models.IntegerField(blank=True, null=True)
    exposure_pattern = models.TextField(blank=True, null=True)  # This field type is a guess.
    exposure_time = models.IntegerField(blank=True, null=True)
    develop_time = models.IntegerField(blank=True, null=True)
    metric_pattern_quality = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_leftover_photoresist = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_missing_photoresist = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_contaminants = models.TextField(blank=True, null=True)  # This field type is a guess.
    metrology_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'patterning'


class PlasmaClean(models.Model):
    id = models.IntegerField()
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    o2_flow = models.TextField(blank=True, null=True)  # This field type is a guess.
    rf_power = models.TextField(blank=True, null=True)  # This field type is a guess.
    clean_time = models.IntegerField(blank=True, null=True)
    metric_contaminants = models.TextField(blank=True, null=True)  # This field type is a guess.
    metrology_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'plasma_clean'


class PlasmaEtch(models.Model):
    id = models.IntegerField()
    chip_number = models.IntegerField()
    chip_owner = models.TextField(blank=True, null=True)  # This field type is a guess.
    creation_date = models.DateField(blank=True, null=True)
    o2_flow = models.TextField(blank=True, null=True)  # This field type is a guess.
    sf6_flow = models.TextField(blank=True, null=True)  # This field type is a guess.
    rf_power = models.TextField(blank=True, null=True)  # This field type is a guess.
    etch_time = models.IntegerField(blank=True, null=True)
    etch_depth = models.TextField(blank=True, null=True)  # This field type is a guess.
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'plasma_etch'

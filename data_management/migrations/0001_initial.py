# Generated by Django 5.0.1 on 2024-04-23 22:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SMU_capture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_current', models.FileField(blank=True, upload_to='')),
                ('csv_voltage', models.FileField(blank=True, upload_to='')),
                ('plot', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ChipList',
            fields=[
                ('chip_number', models.IntegerField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(blank=True)),
                ('notes', models.CharField(blank=True, max_length=400, null=True)),
                ('IVCurrrents_CSV', models.FileField(blank=True, upload_to='')),
                ('IVVoltages_CSV', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AluminumEvaporation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('AluminumEvaporation_step_time', models.DateTimeField(blank=True)),
                ('AluminumEvaporation_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_time', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_pressure_before_start_seq', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_pressure_before_evaporation', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_metric_layer_thickness', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_metric_layer_thick_qcm', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_metric_deposition_rate', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_metrology_link', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEvaporation_notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
            ],
        ),
        migrations.CreateModel(
            name='AluminumEtch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('AluminumEtch_step_time', models.DateTimeField(blank=True)),
                ('AluminumEtch_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEtch_time', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEtch_stir_rpm', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEtch_metric_alum_etch_depth', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEtch_metric_photoresist_peeling', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEtch_metric_aluminum_peeling', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEtch_metrology_link', models.CharField(blank=True, max_length=400, null=True)),
                ('AluminumEtch_notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
            ],
        ),
        migrations.CreateModel(
            name='ChipListSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chip_number', models.IntegerField(blank=True)),
                ('creation_time', models.DateTimeField(blank=True)),
                ('notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('Deposition_step_time', models.DateTimeField(blank=True)),
                ('Deposition_glass_type', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_cleaning_step', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_days_glass_at_room_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_prebake_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_prebake_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_amount_drops', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_spin_rpm', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_spin_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_bake_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_bake_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_humidity', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_metric_layer_thickness', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_metric_cracking', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_metric_particles', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_metrology_link', models.CharField(blank=True, max_length=400, null=True)),
                ('Deposition_notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OxideEtch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('OxideEtch_step_time', models.DateTimeField(blank=True)),
                ('OxideEtch_max_temp_glass_reached', models.CharField(blank=True, max_length=400, null=True)),
                ('OxideEtch_time', models.CharField(blank=True, max_length=400, null=True)),
                ('OxideEtch_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('OxideEtch_metric_oxide_etch_depth', models.CharField(blank=True, max_length=400, null=True)),
                ('OxideEtch_metrology_link', models.CharField(blank=True, max_length=400, null=True)),
                ('OxideEtch_notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patterning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('Patterning_step_time', models.DateTimeField(blank=True)),
                ('Patterning_underlying_material', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_hdms_prebake_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_hdms_prebake_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_hdms_spin_rpm', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_hdms_spin_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_hdms_bake_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_hdms_bake_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_photoresist_spin_rpm', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_photoresist_spin_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_photoresist_bake_temp', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_photoresist_bake_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_exposure_pattern', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_exposure_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_develop_time', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_metric_pattern_quality', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_metric_leftover_photoresist', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_metric_missing_photoresist', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_metric_contaminants', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_metrology_link', models.CharField(blank=True, max_length=400, null=True)),
                ('Patterning_notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlasmaClean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('PlasmaClean_step_time', models.DateTimeField(blank=True)),
                ('PlasmaClean_o2_flow', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaClean_rf_power', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaClean_clean_time', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaClean_metric_contaminants', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaClean_metrology_link', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaClean_notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlasmaEtch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=50)),
                ('PlasmaEtch_step_time', models.DateTimeField(blank=True)),
                ('PlasmaEtch_o2_flow', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaEtch_sf6_flow', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaEtch_rf_power', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaEtch_etch_time', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaEtch_etch_depth', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaEtch_metrology_link', models.CharField(blank=True, max_length=400, null=True)),
                ('PlasmaEtch_notes', models.CharField(blank=True, max_length=400, null=True)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=300)),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(max_length=50)),
                ('followers', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='entry_creators', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IVCurve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drain_resistance', models.IntegerField(default=100)),
                ('gate_resistance', models.IntegerField(default=100)),
                ('device_id', models.CharField(max_length=50)),
                ('gate_voltages', models.CharField(max_length=500)),
                ('chip_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='data_management.chiplist')),
                ('chip_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('captures', models.ManyToManyField(to='data_management.smu_capture')),
            ],
        ),
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class E200317CtValues(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    target_name = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    number_10g_0_25l_30s = models.FloatField(db_column='10G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_25l_90s = models.FloatField(db_column='10G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_30s = models.FloatField(db_column='12.5G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_90s = models.FloatField(db_column='12.5G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_30s = models.FloatField(db_column='15G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_90s = models.FloatField(db_column='15G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_30s = models.FloatField(db_column='17.5G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_90s = models.FloatField(db_column='17.5G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_30s = models.FloatField(db_column='10G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_90s = models.FloatField(db_column='10G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_30s = models.FloatField(db_column='12.5G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_90s = models.FloatField(db_column='12.5G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_30s = models.FloatField(db_column='15G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_90s = models.FloatField(db_column='15G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_30s = models.FloatField(db_column='17.5G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_90s = models.FloatField(db_column='17.5G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_25l_50s = models.FloatField(db_column='10G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_25l_70s = models.FloatField(db_column='10G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_50s = models.FloatField(db_column='12.5G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_70s = models.FloatField(db_column='12.5G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_50s = models.FloatField(db_column='15G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_70s = models.FloatField(db_column='15G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_50s = models.FloatField(db_column='17.5G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_70s = models.FloatField(db_column='17.5G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_50s = models.FloatField(db_column='10G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_70s = models.FloatField(db_column='10G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_50s = models.FloatField(db_column='12.5G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_70s = models.FloatField(db_column='12.5G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_50s = models.FloatField(db_column='15G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_70s = models.FloatField(db_column='15G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_50s = models.FloatField(db_column='17.5G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_70s = models.FloatField(db_column='17.5G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '200317 CT values'


class E200317FoldChange(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    target_name = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    number_10g_0_25l_30s = models.FloatField(db_column='10G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_25l_90s = models.FloatField(db_column='10G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_30s = models.FloatField(db_column='12.5G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_90s = models.FloatField(db_column='12.5G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_30s = models.FloatField(db_column='15G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_90s = models.FloatField(db_column='15G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_30s = models.FloatField(db_column='17.5G_0.25L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_90s = models.FloatField(db_column='17.5G_0.25L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_30s = models.FloatField(db_column='10G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_90s = models.FloatField(db_column='10G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_30s = models.FloatField(db_column='12.5G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_90s = models.FloatField(db_column='12.5G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_30s = models.FloatField(db_column='15G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_90s = models.FloatField(db_column='15G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_30s = models.FloatField(db_column='17.5G_0.5L_30S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_90s = models.FloatField(db_column='17.5G_0.5L_90S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_25l_50s = models.FloatField(db_column='10G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_25l_70s = models.FloatField(db_column='10G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_50s = models.FloatField(db_column='12.5G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_25l_70s = models.FloatField(db_column='12.5G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_50s = models.FloatField(db_column='15G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_25l_70s = models.FloatField(db_column='15G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_50s = models.FloatField(db_column='17.5G_0.25L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_25l_70s = models.FloatField(db_column='17.5G_0.25L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_50s = models.FloatField(db_column='10G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10g_0_5l_70s = models.FloatField(db_column='10G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_50s = models.FloatField(db_column='12.5G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5g_0_5l_70s = models.FloatField(db_column='12.5G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_50s = models.FloatField(db_column='15G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15g_0_5l_70s = models.FloatField(db_column='15G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_50s = models.FloatField(db_column='17.5G_0.5L_50S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5g_0_5l_70s = models.FloatField(db_column='17.5G_0.5L_70S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = '200317 Fold change'


class E200317Parameter(models.Model):
    uuid = models.IntegerField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    gelma_concentration = models.FloatField(db_column='gelma concentration')  # Field renamed to remove unsuitable characters.
    cure_adhesive = models.CharField(db_column='cure adhesive', max_length=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    adhesive_concentration = models.FloatField(db_column='adhesive concentration', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    light_cure_time = models.IntegerField(db_column='light cure time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    print_speed_mm_min_field = models.IntegerField(db_column='print speed(mm/min)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    size_of_tip_g_field = models.IntegerField(db_column='size of tip(G)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    thickness_mm_field = models.IntegerField(db_column='thickness(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    average_tensile_strength = models.FloatField(db_column='Average Tensile Strength', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    std_tensile_strength = models.FloatField(db_column='STD Tensile Strength', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_young_s_modulus = models.FloatField(db_column="Average Young's Modulus", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    std_young_s_modulus = models.FloatField(db_column="STD Young's Modulus", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = '200317 parameter'


class E200317Score(models.Model):
    uuid = models.IntegerField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    sample_name = models.CharField(max_length=30)
    self_renewal = models.FloatField(db_column='self-renewal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ectoderm = models.FloatField(db_column='Ectoderm', blank=True, null=True)  # Field name made lowercase.
    mesoderm = models.FloatField(db_column='Mesoderm', blank=True, null=True)  # Field name made lowercase.
    endoderm = models.FloatField(db_column='Endoderm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '200317 score'


class E201016Parameter(models.Model):
    uuid = models.IntegerField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    gelma_concentration = models.FloatField(db_column='gelma concentration')  # Field renamed to remove unsuitable characters.
    cure_adhesive = models.CharField(db_column='cure adhesive', max_length=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    adhesive_concentration = models.FloatField(db_column='adhesive concentration', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    light_cure_time = models.IntegerField(db_column='light cure time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    print_speed_mm_min_field = models.IntegerField(db_column='print speed(mm/min)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    size_of_tip_g_field = models.IntegerField(db_column='size of tip(G)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    thickness_mm_field = models.IntegerField(db_column='thickness(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    average_tensile_strength = models.FloatField(db_column='Average Tensile Strength', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    std_tensile_strength = models.FloatField(db_column='STD Tensile Strength', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_young_s_modulus = models.FloatField(db_column="Average Young's Modulus", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    std_young_s_modulus = models.FloatField(db_column="STD Young's Modulus", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    self_renewal_discrete_field = models.CharField(db_column='Self-renewal(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ectoderm_discrete_field = models.CharField(db_column='Ectoderm(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mesoderm_discrete_field = models.CharField(db_column='Mesoderm(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    endoderm_discrete_field = models.CharField(db_column='Endoderm(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    self_renewal = models.FloatField(db_column='Self-renewal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ectoderm = models.FloatField(db_column='Ectoderm', blank=True, null=True)  # Field name made lowercase.
    mesoderm = models.FloatField(db_column='Mesoderm', blank=True, null=True)  # Field name made lowercase.
    endoderm = models.FloatField(db_column='Endoderm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 parameter'


class E201016Score(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    self_renewal_discrete_field = models.CharField(db_column='Self-renewal(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ectoderm_discrete_field = models.CharField(db_column='Ectoderm(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mesoderm_discrete_field = models.CharField(db_column='Mesoderm(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    endoderm_discrete_field = models.CharField(db_column='Endoderm(discrete)', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    self_renewal = models.FloatField(db_column='self-renewal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ectoderm = models.FloatField(db_column='Ectoderm', blank=True, null=True)  # Field name made lowercase.
    mesoderm = models.FloatField(db_column='Mesoderm', blank=True, null=True)  # Field name made lowercase.
    endoderm = models.FloatField(db_column='Endoderm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 score'
      
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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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

class ScorecardCtValues(models.Model):
    target = models.CharField(primary_key=True, max_length=30)
    category = models.CharField(max_length=20, blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scorecard CT values'
        app_label = "contents"

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class E1227SimulationResult(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    gelma_concentration = models.FloatField(blank=True, null=True)
    cure_adhesive = models.CharField(max_length=10, blank=True, null=True)
    adhesive_concentration = models.FloatField(blank=True, null=True)
    light_cure_time = models.IntegerField(blank=True, null=True)
    groove_angle = models.IntegerField(blank=True, null=True)
    maxmises = models.FloatField(db_column='maxMises', blank=True, null=True)  # Field name made lowercase.
    maxprincipal = models.FloatField(db_column='maxPrincipal', blank=True, null=True)  # Field name made lowercase.
    minprincipal = models.FloatField(db_column='minPrincipal', blank=True, null=True)  # Field name made lowercase.
    convergence = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '1227 simulation result'


class E201016CtValuesControl(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    actb = models.FloatField(db_column='ACTB', blank=True, null=True)  # Field name made lowercase.
    actb_1 = models.FloatField(db_column='ACTB_1', blank=True, null=True)  # Field name made lowercase.
    actb_2 = models.FloatField(db_column='ACTB_2', blank=True, null=True)  # Field name made lowercase.
    actb_3 = models.FloatField(db_column='ACTB_3', blank=True, null=True)  # Field name made lowercase.
    ctcf = models.FloatField(db_column='CTCF', blank=True, null=True)  # Field name made lowercase.
    ep300 = models.FloatField(db_column='EP300', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 CT values control'


class E201016CtValuesMesendoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    fgf4 = models.FloatField(db_column='FGF4', blank=True, null=True)  # Field name made lowercase.
    gdf3 = models.FloatField(db_column='GDF3', blank=True, null=True)  # Field name made lowercase.
    nppb = models.FloatField(db_column='NPPB', blank=True, null=True)  # Field name made lowercase.
    nr5a2 = models.FloatField(db_column='NR5A2', blank=True, null=True)  # Field name made lowercase.
    pthlh = models.FloatField(db_column='PTHLH', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 CT values mesendoderm'


class E201016CtValuesMesoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    abca4 = models.FloatField(db_column='ABCA4', blank=True, null=True)  # Field name made lowercase.
    alox15 = models.FloatField(db_column='ALOX15', blank=True, null=True)  # Field name made lowercase.
    bmp10 = models.FloatField(db_column='BMP10', blank=True, null=True)  # Field name made lowercase.
    cdh5 = models.FloatField(db_column='CDH5', blank=True, null=True)  # Field name made lowercase.
    cdx2 = models.FloatField(db_column='CDX2', blank=True, null=True)  # Field name made lowercase.
    colec10 = models.FloatField(db_column='COLEC10', blank=True, null=True)  # Field name made lowercase.
    esm1 = models.FloatField(db_column='ESM1', blank=True, null=True)  # Field name made lowercase.
    fcn3 = models.FloatField(db_column='FCN3', blank=True, null=True)  # Field name made lowercase.
    foxf1 = models.FloatField(db_column='FOXF1', blank=True, null=True)  # Field name made lowercase.
    hand1 = models.FloatField(db_column='HAND1', blank=True, null=True)  # Field name made lowercase.
    hand2 = models.FloatField(db_column='HAND2', blank=True, null=True)  # Field name made lowercase.
    hey1 = models.FloatField(db_column='HEY1', blank=True, null=True)  # Field name made lowercase.
    hopx = models.FloatField(db_column='HOPX', blank=True, null=True)  # Field name made lowercase.
    il6st = models.FloatField(db_column='IL6ST', blank=True, null=True)  # Field name made lowercase.
    nkx2_5 = models.FloatField(db_column='NKX2-5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    odam = models.FloatField(db_column='ODAM', blank=True, null=True)  # Field name made lowercase.
    pdgfra = models.FloatField(db_column='PDGFRA', blank=True, null=True)  # Field name made lowercase.
    plvap = models.FloatField(db_column='PLVAP', blank=True, null=True)  # Field name made lowercase.
    rgs4 = models.FloatField(db_column='RGS4', blank=True, null=True)  # Field name made lowercase.
    snai2 = models.FloatField(db_column='SNAI2', blank=True, null=True)  # Field name made lowercase.
    tbx3 = models.FloatField(db_column='TBX3', blank=True, null=True)  # Field name made lowercase.
    tm4sf1 = models.FloatField(db_column='TM4SF1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 CT values mesoderm'


class E201016CtValuesSelfrenewal(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    dnmt3b = models.FloatField(db_column='DNMT3B', blank=True, null=True)  # Field name made lowercase.
    hesx1 = models.FloatField(db_column='HESX1', blank=True, null=True)  # Field name made lowercase.
    ido1 = models.FloatField(db_column='IDO1', blank=True, null=True)  # Field name made lowercase.
    lck = models.FloatField(db_column='LCK', blank=True, null=True)  # Field name made lowercase.
    nanog = models.FloatField(db_column='NANOG', blank=True, null=True)  # Field name made lowercase.
    pou5f1 = models.FloatField(db_column='POU5F1', blank=True, null=True)  # Field name made lowercase.
    sox2 = models.FloatField(db_column='SOX2', blank=True, null=True)  # Field name made lowercase.
    trim22 = models.FloatField(db_column='TRIM22', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 CT values selfrenewal'


class E201016DctValueEctoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    cdh9 = models.FloatField(db_column='CDH9', blank=True, null=True)  # Field name made lowercase.
    col2a1 = models.FloatField(db_column='COL2A1', blank=True, null=True)  # Field name made lowercase.
    dmbx1 = models.FloatField(db_column='DMBX1', blank=True, null=True)  # Field name made lowercase.
    drd4 = models.FloatField(db_column='DRD4', blank=True, null=True)  # Field name made lowercase.
    en1 = models.FloatField(db_column='EN1', blank=True, null=True)  # Field name made lowercase.
    lmx1a = models.FloatField(db_column='LMX1A', blank=True, null=True)  # Field name made lowercase.
    map2 = models.FloatField(db_column='MAP2', blank=True, null=True)  # Field name made lowercase.
    myo3b = models.FloatField(db_column='MYO3B', blank=True, null=True)  # Field name made lowercase.
    nos2 = models.FloatField(db_column='NOS2', blank=True, null=True)  # Field name made lowercase.
    nr2f1_nr2f2 = models.FloatField(db_column='NR2F1-NR2F2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nr2f2 = models.FloatField(db_column='NR2F2', blank=True, null=True)  # Field name made lowercase.
    olfm3 = models.FloatField(db_column='OLFM3', blank=True, null=True)  # Field name made lowercase.
    papln = models.FloatField(db_column='PAPLN', blank=True, null=True)  # Field name made lowercase.
    pax3 = models.FloatField(db_column='PAX3', blank=True, null=True)  # Field name made lowercase.
    pax6 = models.FloatField(db_column='PAX6', blank=True, null=True)  # Field name made lowercase.
    pou4f1 = models.FloatField(db_column='POU4F1', blank=True, null=True)  # Field name made lowercase.
    prkca = models.FloatField(db_column='PRKCA', blank=True, null=True)  # Field name made lowercase.
    sdc2 = models.FloatField(db_column='SDC2', blank=True, null=True)  # Field name made lowercase.
    sox1 = models.FloatField(db_column='SOX1', blank=True, null=True)  # Field name made lowercase.
    trpm8 = models.FloatField(db_column='TRPM8', blank=True, null=True)  # Field name made lowercase.
    wnt1 = models.FloatField(db_column='WNT1', blank=True, null=True)  # Field name made lowercase.
    zbtb16 = models.FloatField(db_column='ZBTB16', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 DCT value ectoderm'


class E201016DctValueEndoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    afp = models.FloatField(db_column='AFP', blank=True, null=True)  # Field name made lowercase.
    cabp7 = models.FloatField(db_column='CABP7', blank=True, null=True)  # Field name made lowercase.
    cdh20 = models.FloatField(db_column='CDH20', blank=True, null=True)  # Field name made lowercase.
    cldn1 = models.FloatField(db_column='CLDN1', blank=True, null=True)  # Field name made lowercase.
    cplx2 = models.FloatField(db_column='CPLX2', blank=True, null=True)  # Field name made lowercase.
    elavl3 = models.FloatField(db_column='ELAVL3', blank=True, null=True)  # Field name made lowercase.
    eomes = models.FloatField(db_column='EOMES', blank=True, null=True)  # Field name made lowercase.
    foxa1 = models.FloatField(db_column='FOXA1', blank=True, null=True)  # Field name made lowercase.
    foxa2 = models.FloatField(db_column='FOXA2', blank=True, null=True)  # Field name made lowercase.
    foxp2 = models.FloatField(db_column='FOXP2', blank=True, null=True)  # Field name made lowercase.
    gata4 = models.FloatField(db_column='GATA4', blank=True, null=True)  # Field name made lowercase.
    gata6 = models.FloatField(db_column='GATA6', blank=True, null=True)  # Field name made lowercase.
    hhex = models.FloatField(db_column='HHEX', blank=True, null=True)  # Field name made lowercase.
    hmp19 = models.FloatField(db_column='HMP19', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    klf5 = models.FloatField(db_column='KLF5', blank=True, null=True)  # Field name made lowercase.
    lefty1 = models.FloatField(db_column='LEFTY1', blank=True, null=True)  # Field name made lowercase.
    lefty2 = models.FloatField(db_column='LEFTY2', blank=True, null=True)  # Field name made lowercase.
    nodal = models.FloatField(db_column='NODAL', blank=True, null=True)  # Field name made lowercase.
    phox2b = models.FloatField(db_column='PHOX2B', blank=True, null=True)  # Field name made lowercase.
    pou3f3 = models.FloatField(db_column='POU3F3', blank=True, null=True)  # Field name made lowercase.
    prdm1 = models.FloatField(db_column='PRDM1', blank=True, null=True)  # Field name made lowercase.
    rxrg = models.FloatField(db_column='RXRG', blank=True, null=True)  # Field name made lowercase.
    sox17 = models.FloatField(db_column='SOX17', blank=True, null=True)  # Field name made lowercase.
    sst = models.FloatField(db_column='SST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 DCT value endoderm'


class E201016DctValueOther(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    cd44 = models.FloatField(db_column='CD44', blank=True, null=True)  # Field name made lowercase.
    jarid2 = models.FloatField(db_column='JARID2', blank=True, null=True)  # Field name made lowercase.
    myc = models.FloatField(db_column='MYC', blank=True, null=True)  # Field name made lowercase.
    sev = models.FloatField(db_column='SEV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 DCT value other'


class E201016FoldChangeEctoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    cdh9 = models.FloatField(db_column='CDH9', blank=True, null=True)  # Field name made lowercase.
    col2a1 = models.FloatField(db_column='COL2A1', blank=True, null=True)  # Field name made lowercase.
    dmbx1 = models.FloatField(db_column='DMBX1', blank=True, null=True)  # Field name made lowercase.
    drd4 = models.FloatField(db_column='DRD4', blank=True, null=True)  # Field name made lowercase.
    en1 = models.FloatField(db_column='EN1', blank=True, null=True)  # Field name made lowercase.
    lmx1a = models.FloatField(db_column='LMX1A', blank=True, null=True)  # Field name made lowercase.
    map2 = models.FloatField(db_column='MAP2', blank=True, null=True)  # Field name made lowercase.
    myo3b = models.FloatField(db_column='MYO3B', blank=True, null=True)  # Field name made lowercase.
    nos2 = models.FloatField(db_column='NOS2', blank=True, null=True)  # Field name made lowercase.
    nr2f1_nr2f2 = models.FloatField(db_column='NR2F1-NR2F2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nr2f2 = models.FloatField(db_column='NR2F2', blank=True, null=True)  # Field name made lowercase.
    olfm3 = models.FloatField(db_column='OLFM3', blank=True, null=True)  # Field name made lowercase.
    papln = models.FloatField(db_column='PAPLN', blank=True, null=True)  # Field name made lowercase.
    pax3 = models.FloatField(db_column='PAX3', blank=True, null=True)  # Field name made lowercase.
    pax6 = models.FloatField(db_column='PAX6', blank=True, null=True)  # Field name made lowercase.
    pou4f1 = models.FloatField(db_column='POU4F1', blank=True, null=True)  # Field name made lowercase.
    prkca = models.FloatField(db_column='PRKCA', blank=True, null=True)  # Field name made lowercase.
    sdc2 = models.FloatField(db_column='SDC2', blank=True, null=True)  # Field name made lowercase.
    sox1 = models.FloatField(db_column='SOX1', blank=True, null=True)  # Field name made lowercase.
    trpm8 = models.FloatField(db_column='TRPM8', blank=True, null=True)  # Field name made lowercase.
    wnt1 = models.FloatField(db_column='WNT1', blank=True, null=True)  # Field name made lowercase.
    zbtb16 = models.FloatField(db_column='ZBTB16', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 Fold change ectoderm'


class E201016FoldChangeEndoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    afp = models.FloatField(db_column='AFP', blank=True, null=True)  # Field name made lowercase.
    cabp7 = models.FloatField(db_column='CABP7', blank=True, null=True)  # Field name made lowercase.
    cdh20 = models.FloatField(db_column='CDH20', blank=True, null=True)  # Field name made lowercase.
    cldn1 = models.FloatField(db_column='CLDN1', blank=True, null=True)  # Field name made lowercase.
    cplx2 = models.FloatField(db_column='CPLX2', blank=True, null=True)  # Field name made lowercase.
    elavl3 = models.FloatField(db_column='ELAVL3', blank=True, null=True)  # Field name made lowercase.
    eomes = models.FloatField(db_column='EOMES', blank=True, null=True)  # Field name made lowercase.
    foxa1 = models.FloatField(db_column='FOXA1', blank=True, null=True)  # Field name made lowercase.
    foxa2 = models.FloatField(db_column='FOXA2', blank=True, null=True)  # Field name made lowercase.
    foxp2 = models.FloatField(db_column='FOXP2', blank=True, null=True)  # Field name made lowercase.
    gata4 = models.FloatField(db_column='GATA4', blank=True, null=True)  # Field name made lowercase.
    gata6 = models.FloatField(db_column='GATA6', blank=True, null=True)  # Field name made lowercase.
    hhex = models.FloatField(db_column='HHEX', blank=True, null=True)  # Field name made lowercase.
    hmp19 = models.FloatField(db_column='HMP19', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    klf5 = models.FloatField(db_column='KLF5', blank=True, null=True)  # Field name made lowercase.
    lefty1 = models.FloatField(db_column='LEFTY1', blank=True, null=True)  # Field name made lowercase.
    lefty2 = models.FloatField(db_column='LEFTY2', blank=True, null=True)  # Field name made lowercase.
    nodal = models.FloatField(db_column='NODAL', blank=True, null=True)  # Field name made lowercase.
    phox2b = models.FloatField(db_column='PHOX2B', blank=True, null=True)  # Field name made lowercase.
    pou3f3 = models.FloatField(db_column='POU3F3', blank=True, null=True)  # Field name made lowercase.
    prdm1 = models.FloatField(db_column='PRDM1', blank=True, null=True)  # Field name made lowercase.
    rxrg = models.FloatField(db_column='RXRG', blank=True, null=True)  # Field name made lowercase.
    sox17 = models.FloatField(db_column='SOX17', blank=True, null=True)  # Field name made lowercase.
    sst = models.FloatField(db_column='SST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 Fold change endoderm'


class E201016FoldChangeMesendoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    fgf4 = models.FloatField(db_column='FGF4', blank=True, null=True)  # Field name made lowercase.
    gdf3 = models.FloatField(db_column='GDF3', blank=True, null=True)  # Field name made lowercase.
    nppb = models.FloatField(db_column='NPPB', blank=True, null=True)  # Field name made lowercase.
    nr5a2 = models.FloatField(db_column='NR5A2', blank=True, null=True)  # Field name made lowercase.
    pthlh = models.FloatField(db_column='PTHLH', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 Fold change mesendoderm'


class E201016FoldChangeMesoderm(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    abca4 = models.FloatField(db_column='ABCA4', blank=True, null=True)  # Field name made lowercase.
    alox15 = models.FloatField(db_column='ALOX15', blank=True, null=True)  # Field name made lowercase.
    bmp10 = models.FloatField(db_column='BMP10', blank=True, null=True)  # Field name made lowercase.
    cdh5 = models.FloatField(db_column='CDH5', blank=True, null=True)  # Field name made lowercase.
    cdx2 = models.FloatField(db_column='CDX2', blank=True, null=True)  # Field name made lowercase.
    colec10 = models.FloatField(db_column='COLEC10', blank=True, null=True)  # Field name made lowercase.
    esm1 = models.FloatField(db_column='ESM1', blank=True, null=True)  # Field name made lowercase.
    fcn3 = models.FloatField(db_column='FCN3', blank=True, null=True)  # Field name made lowercase.
    foxf1 = models.FloatField(db_column='FOXF1', blank=True, null=True)  # Field name made lowercase.
    hand1 = models.FloatField(db_column='HAND1', blank=True, null=True)  # Field name made lowercase.
    hand2 = models.FloatField(db_column='HAND2', blank=True, null=True)  # Field name made lowercase.
    hey1 = models.FloatField(db_column='HEY1', blank=True, null=True)  # Field name made lowercase.
    hopx = models.FloatField(db_column='HOPX', blank=True, null=True)  # Field name made lowercase.
    il6st = models.FloatField(db_column='IL6ST', blank=True, null=True)  # Field name made lowercase.
    nkx2_5 = models.FloatField(db_column='NKX2-5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    odam = models.FloatField(db_column='ODAM', blank=True, null=True)  # Field name made lowercase.
    pdgfra = models.FloatField(db_column='PDGFRA', blank=True, null=True)  # Field name made lowercase.
    plvap = models.FloatField(db_column='PLVAP', blank=True, null=True)  # Field name made lowercase.
    rgs4 = models.FloatField(db_column='RGS4', blank=True, null=True)  # Field name made lowercase.
    snai2 = models.FloatField(db_column='SNAI2', blank=True, null=True)  # Field name made lowercase.
    tbx3 = models.FloatField(db_column='TBX3', blank=True, null=True)  # Field name made lowercase.
    tm4sf1 = models.FloatField(db_column='TM4SF1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 Fold change mesoderm'


class E201016FoldChangeSelfrenewal(models.Model):
    uuid = models.AutoField(db_column='UUID', primary_key=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    dnmt3b = models.FloatField(db_column='DNMT3B', blank=True, null=True)  # Field name made lowercase.
    hesx1 = models.FloatField(db_column='HESX1', blank=True, null=True)  # Field name made lowercase.
    ido1 = models.FloatField(db_column='IDO1', blank=True, null=True)  # Field name made lowercase.
    lck = models.FloatField(db_column='LCK', blank=True, null=True)  # Field name made lowercase.
    nanog = models.FloatField(db_column='NANOG', blank=True, null=True)  # Field name made lowercase.
    pou5f1 = models.FloatField(db_column='POU5F1', blank=True, null=True)  # Field name made lowercase.
    sox2 = models.FloatField(db_column='SOX2', blank=True, null=True)  # Field name made lowercase.
    trim22 = models.FloatField(db_column='TRIM22', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '201016 Fold change selfrenewal'


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

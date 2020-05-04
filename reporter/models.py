from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager


# Create your models here.
class Incidences(models.Model):
    name = models.TextField()
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"

class Counties(models.Model):
    gid_0 = models.CharField(max_length=80, null=True, blank=True)
    name_0 = models.CharField(max_length=80, null=True, blank=True)
    gid_1 = models.CharField(max_length=80, null=True, blank=True)
    name_1 = models.CharField(max_length=80, null=True, blank=True)
    gid_2 = models.CharField(max_length=80, null=True, blank=True)
    name_2 = models.CharField(max_length=80, null=True, blank=True)
    gid_3 = models.CharField(max_length=80, null=True, blank=True)
    name_3 = models.CharField(max_length=80, null=True, blank=True)
    gid_4 = models.CharField(max_length=80, null=True, blank=True)
    name_4 = models.CharField(max_length=80, null=True, blank=True)
    varname_4 = models.CharField(max_length=80, null=True, blank=True)
    type_4 = models.CharField(max_length=80, null=True, blank=True)
    engtype_4 = models.CharField(max_length=80, null=True, blank=True)
    cc_4 = models.CharField(max_length=80, null=True, blank=True)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name_4

    def __unicode__(self):
        return self.name_4

    class Meta:
        verbose_name_plural = 'Counties'
        


from django.db import models
from django.contrib.postgres.fields import JSONField

class grid(models.Model):
    lat_lon = models.FloatField(blank=True,null=True)
    coor = models.FloatField(blank=True,null=True)

class cli_ind(models.Model):
    su = JSONField(default=[])
    fd = JSONField(default={})
    Id = JSONField(default=[])
    tr = JSONField(default=[])
    # longitude = models.DecimalField(max_digits=9, decimal_places=5)
    # latitude = models.DecimalField(max_digits=9, decimal_places=5)
    # default={}
    # testf = models.FloatField(blank=True,null=True)
    # coordinate = ArrayField(models.DecimalField(max_digits=9, decimal_places=5), blank=True)



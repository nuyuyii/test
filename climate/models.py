from django.db import models
from django.contrib.postgres.fields import JSONField

class feature(models.Model):
    point = JSONField(default=[])
    climdex = JSONField(default={})
    coordinates = JSONField(default=[])
    # longitude = models.DecimalField(max_digits=9, decimal_places=5)
    # latitude = models.DecimalField(max_digits=9, decimal_places=5)
    # default={}
    # testf = models.FloatField(blank=True,null=True)
    # coordinate = ArrayField(models.DecimalField(max_digits=9, decimal_places=5), blank=True)


class Ts(models.Model):
    data = JSONField()

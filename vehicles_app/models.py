from django.db import models


class Vehicle(models.Model):
    make = models.CharField(max_length=255, null=True, default=None)
    model = models.CharField(max_length=255, null=True, default=None)
    speed = models.IntegerField(default=None, null=True)
    average_speed = models.IntegerField(default=None, null=True)
    temperature = models.FloatField(default=None, null=True)
    fuel_level = models.IntegerField(default=None, null=True)
    engine_status = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return "Vehicle(%s): make: %s, model: %s" % (self.id, self.make, self.model)

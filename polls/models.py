from django.db import models


class Campaign(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Creative(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    panel_id = models.IntegerField()


class Booking(models.Model):
    booking_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    creative_id = models.ForeignKey(Creative, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

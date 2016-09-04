from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from locations.models import Location
from django.conf import settings


class Wait(models.Model):
    star_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total_time = models.PositiveSmallIntegerField(null=True, blank=True)
    rating = models.DecimalField(validators=[MinValueValidator(1), MaxValueValidator(5)], max_digits=2,
                                 decimal_places=1, blank=True, null=True)
    rating_comment = models.CharField(max_length=1000, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='waits_for_user')
    location = models.ForeignKey(Location, related_name='waits_for_location')

    def __str__(self):
        return u"Location: {0}, User: {1}, Time range: {2} - {3}".format(
                self.location_id,
                self.user_id,
                self.star_time.strftime("%Y-%m-%d %H:%M:%S"),
                self.end_time.strftime("%Y-%m-%d %H:%M:%S")
        )

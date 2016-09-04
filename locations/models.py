from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Location(models.Model):
    TYPE_CHOICES = (
        ('hospital', 'Hospital'),
        ('walk_in_clinic', 'Walk in Clinic')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=45, db_index=True)
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=45, blank=True)
    postal_code = models.CharField(max_length=45, blank=True)
    state = models.CharField(max_length=45, blank=True)
    country = models.CharField(max_length=45, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, db_index=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, db_index=True)
    summary = models.TextField(blank=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    hours_of_operation = models.CharField(max_length=45)
    rating = models.DecimalField(validators=[MinValueValidator(1), MaxValueValidator(5)], max_digits=2,
                                 decimal_places=1, blank=True, null=True)
    number_of_wait_samples = models.IntegerField(default=0)
    total_wait = models.IntegerField(default=0)

    def __str__(self):
        return u"{0} ({1})".format(self.name, self.get_type_display())

    class Meta:
        ordering = ('-id',)

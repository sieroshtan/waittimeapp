from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=45, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    number_of_wait_samples = models.IntegerField(default=0)
    total_wait = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ('email',)

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

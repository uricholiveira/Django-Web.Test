from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import pycountry
from operator import itemgetter

# these are model abstracts from django extensions
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel
)

countries = sorted(
    [(country.name, country.name) for country in pycountry.countries], key=itemgetter(0)
)
countries.insert(0, ("Select Country", "Select Country"))


class UserProfile(TimeStampedModel, ActivatorModel, models.Model):
    """
    users.UserProfile

    Stores a single user profile related to :model:`auth.User`
    """

    class Meta:
        verbose_name_plural = 'User Profiles'
        ordering = ['id']

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="Phone number", max_length=14, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True, choices=countries)

    @property
    def country_alpha_2(self):
        """
        Used to return the selected country alpha 2 repr i.e. England == GB
        """
        if self.country:
            return pycountry.countries.get(name=self.country).alpha_2

    def __str__(self):
        return self.user.email

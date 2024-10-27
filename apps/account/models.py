from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    phone_number =models.CharField(_("Phone number"), max_length=11)
    is_provider = models.BooleanField(_("Is provider"), default=False)
    is_customer = models.BooleanField(_("Is customer"), default=False)

    def __str__(self) -> str:
            return f"{self.username}"

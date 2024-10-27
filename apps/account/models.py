from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .validator import validate_username, validate_first_name, validate_last_name, validate_password, validate_phone_number
from django.core.validators import validate_email

class User(AbstractUser):
    username = models.CharField(_("username"),max_length=100,unique=True,validators=[validate_username])
    email = models.EmailField(_("email address"), blank=True, validators=[validate_email])
    password = models.CharField(_("password"), max_length=128, validators=[validate_password])
    first_name = models.CharField(_("First name"), max_length=100, validators=[validate_first_name])
    last_name = models.CharField(_("Last name"), max_length=100, validators=[validate_last_name])
    phone_number =models.CharField(_("Phone number"), max_length=11, validators=[validate_phone_number])
    is_provider = models.BooleanField(_("Is provider"), default=False)
    is_customer = models.BooleanField(_("Is customer"), default=False)

    def __str__(self) -> str:
            return f"{self.username}"

from profanity_check import predict_prob
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from string import ascii_lowercase, ascii_uppercase, digits, whitespace, punctuation

def validate_username(username):
    if len(username) < 4:
        raise ValidationError(_("Min length of username must be 4."))
    if len(username) > 100:
        raise ValidationError(_("Max length of username must be 100."))
    
    if (predict_prob([username]))[0] > 0.7:
        raise ValidationError(_("The username has offensive word."))

def validate_password(password):
    if len(password) < 8:
        raise ValidationError(_("Password must be at least 8 characters."))
    if not any([char in ascii_uppercase for char in password]):
        raise ValidationError(_("Password must has uppercase character."))
    if not any([char in ascii_lowercase for char in password]):
        raise ValidationError(_("Password must has lower character."))
    if not any([char in digits for char in password]):
        raise ValidationError(_("Password must has digit character."))
    if any([char in whitespace for char in password]):
        raise ValidationError(_("Password mustn't have whitespace character."))
    if any([char in punctuation for char in password]):
        raise ValidationError(_("Password must has punctuation character."))

def validate_first_name(first_name):
    if (predict_prob([first_name]))[0] > 0.7:
        raise ValidationError(_("The first name has offensive word."))

def validate_last_name(last_name):
    if (predict_prob([last_name]))[0] > 0.7:
        raise ValidationError(_("The last name has offensive word."))

def validate_phone_number(phone_number):
    if not all([char in digits for char in phone_number]):
        raise ValidationError(_("Password must has digit character."))
    if not phone_number.startswith("09"):
        raise ValidationError(_("Phone number must starts with 09 digits."))
    if len(phone_number) != 11:
        raise ValidationError(_("Phone number must be 11 digits."))
    

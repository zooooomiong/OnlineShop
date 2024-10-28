from profanity_check import predict_prob
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from string import ascii_lowercase, ascii_uppercase, digits, whitespace, punctuation


def validate_username(username, with_raise=True):
    errors = []
    if len(username) < 4:
        errors.append(_("Min length of username must be 4."))
    if len(username) > 100:
        errors.append(_("Max length of username must be 100."))
    if (predict_prob([username]))[0] > 0.7:
        errors.append(_("The username has offensive word."))
    if errors and with_raise:
        raise ValidationError(errors)
    return errors


def validate_password(password, with_raise=True):
    errors = []
    if len(password) < 8:
        errors.append(_("Password must be at least 8 characters."))
    if not any([char in ascii_uppercase for char in password]):
        errors.append(_("Password must has uppercase character."))
    if not any([char in ascii_lowercase for char in password]):
        errors.append(_("Password must has lower character."))
    if not any([char in digits for char in password]):
        errors.append(_("Password must has digit character."))
    if any([char in whitespace for char in password]):
        errors.append(_("Password mustn't have whitespace character."))
    if any([char in punctuation for char in password]):
        errors.append(_("Password must has punctuation character."))

    if errors and with_raise:
        raise ValidationError(errors)
    return errors


def validate_first_name(first_name, with_raise=True):
    if (predict_prob([first_name]))[0] > 0.7:
        if with_raise:
            raise ValidationError(_("The first name has offensive word."))
        return [_("The first name has offensive word.")]


def validate_last_name(last_name, with_raise=True):
    if (predict_prob([last_name]))[0] > 0.7:
        if with_raise:
            raise ValidationError([_("The last name has offensive word.")])
        return [_("The last name has offensive word")]


def validate_phone_number(phone_number, with_raise=True):
    errors = []

    if not all([char in digits for char in phone_number]):
        errors.append(_("Phone number must has digit character."))
    if not phone_number.startswith("09"):
        errors.append(_("Phone number must starts with 09 digits."))
    if len(phone_number) != 11:
        errors.append(_("Phone number must be 11 digits."))

    if errors and with_raise:
        raise ValidationError(errors)
    return errors
    
def validate_email(email, with_raise=True):
    import re
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if not re.fullmatch(regex, email):
        if with_raise:
            raise ValidationError([_("Invalid email.")])

        return [_("Invalid email.")]
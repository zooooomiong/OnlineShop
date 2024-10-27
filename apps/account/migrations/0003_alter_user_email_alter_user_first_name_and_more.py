# Generated by Django 5.0.4 on 2024-10-27 20:29

import account.validator
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True,
                max_length=254,
                validators=[django.core.validators.EmailValidator()],
                verbose_name="email address",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                max_length=100,
                validators=[account.validator.validate_first_name],
                verbose_name="First name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                max_length=100,
                validators=[account.validator.validate_last_name],
                verbose_name="Last name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                max_length=128,
                validators=[account.validator.validate_password],
                verbose_name="password",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                max_length=11,
                validators=[account.validator.validate_phone_number],
                verbose_name="Phone number",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=100,
                unique=True,
                validators=[account.validator.validate_username],
                verbose_name="username",
            ),
        ),
    ]
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from account.models import User
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = "*Create User*"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--username", type=str, help="Username for the User")
        parser.add_argument("--email", type=str, help="Email for the User")
        parser.add_argument("--password", type=str, help="Password for the User")

        parser.add_argument("--first_name", type=str, help="First name for the User")
        parser.add_argument("--last_name", type=str, help="Last name for the User")

        # Use store_true/store_false to handle booleans correctly
        parser.add_argument(
            "--is_provider", action="store_true", help="Is Provider for the User"
        )
        parser.add_argument(
            "--is_customer", action="store_true", help="Is Customer for the User"
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        username = options.get("username") or input("Username: ")
        email = options.get("email") or input("Email: ")
        password = options.get("password") or input("Password: ")
        first_name = options.get("first_name") or input("Firstname: ")
        last_name = options.get("last_name") or input("Lastname: ")
        is_provider = options.get("is_provider", False) or bool(input("Is Provider: "))
        is_customer = options.get("is_customer", False) or bool(input("Is customer: "))

        # Validation for required fields
        if not username or not email or not password:
            raise ValidationError("Username, email, and password are required.")

        # Check for unique username
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists (must be unique).")

        # Create the user
        user = User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_provider=is_provider,
            is_customer=is_customer,
        )
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"User created.\nUsername: {username} -- Email: {email}\n"
                f"First Name: {first_name} -- Last Name: {last_name}\n"
                f"Is Provider: {is_provider} -- Is Customer: {is_customer}"
            )
        )

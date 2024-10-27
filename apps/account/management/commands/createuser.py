from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from account.models import User
from django.core.validators import validate_email
from account.validator import (
    validate_username,
    validate_first_name,
    validate_last_name,
    validate_password,
)


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
        try:
            username = options.get("username", "")
            while not username:
                username = input("Username: ")
                try:   
                    validate_username(username)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"{e}"))
                    username = ""
                
                if User.objects.filter(username=username).exists():
                    self.stdout.write(
                        self.style.ERROR("Username already exists (must be unique) try another username.")
                    )
                    username = ""

                            
            
            email = options.get("email", "")
            while not email:
                email = input("Email: ")
                try:   
                    validate_email(email)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"{e}"))
                    email = ""
            
            password = options.get("password", "")
            while not password:
                password = input("Password: ")
                try:
                    validate_password(password)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"{e}"))
                    password = ""
            
            first_name = options.get("first_name", "")
            while not first_name:
                first_name = input("first_name: ")
                try:
                    validate_first_name(first_name)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"{e}"))
                    first_name = ""
            
            last_name = options.get("last_name", "")
            while not last_name:
                last_name = input("last_name: ")
                try:
                    validate_last_name(last_name)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"{e}"))
                    last_name = ""
                    
            is_provider = options.get("is_provider", False) or bool(input("Is Provider: "))
            is_customer = options.get("is_customer", False) or bool(input("Is customer: "))

    
           
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

        
        except EOFError:
            print("CTRL+C")

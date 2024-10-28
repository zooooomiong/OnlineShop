from django import forms
from account.models import User
from .validator import (
    validate_username, validate_first_name, validate_last_name,
    validate_password, validate_phone_number, validate_email
)


class SignupForm(forms.ModelForm):
    field_order = ["username", "first_name", "last_name", "email", "phone_number", "password", "confirm_password"]
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(), max_length=128, required=True
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "phone_number", "password")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "email": forms.EmailInput(attrs={"class": "form-control", "required": True}),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "pattern": r"^09\d{9}$", "required": True, "max_length": 11}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "required": True}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "required": True}),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            self.add_error("username", "This username is already taken. Please choose a different one.")


        for error in validate_username(username, with_raise=False, check_unique=True):
            self.add_error("username", error)
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        for error in validate_email(email, with_raise=False):
            self.add_error("email", error)
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        for error in validate_phone_number(phone_number, with_raise=False):
            self.add_error("phone_number", error)
        return phone_number

    def clean_password(self):
        password = self.cleaned_data.get("password")
        for error in validate_password(password, with_raise=False):
            self.add_error("password", error)
        return password

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        for error in validate_first_name(first_name, with_raise=False):
            self.add_error("first_name", error)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        for error in validate_last_name(last_name, with_raise=False):
            self.add_error("last_name", error)
        return last_name

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Confirm password does not match the password.")

        return cleaned_data

    def create(self):
        user = User.objects.create(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            phone_number=self.cleaned_data["phone_number"],
        )
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

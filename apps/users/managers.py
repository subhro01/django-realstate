from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    """
        Defines a custom user model inheriting the BaseUserManager 
        to create the user from scratch
    """

    def email_validator(self, email):
        """
            Validates if the email address provided is valid or not
        """
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))
        
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        """
            Create and save user using the custom model defined
        """
        
        if not username:
            raise ValueError(_("User must submit a username"))
        if not first_name:
            raise ValueError(_("User must submit a first name"))
        if not last_name:
            raise ValueError(_("User must submit a last name"))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))
        
        user = self.model(
            username=username, first_name=first_name, last_name=last_name, email=email, **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        """
            Creates the superuser using the custom user model defined
        """
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        
        if not password:
            raise ValueError(_("Superusers must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin account: an email address is required"))

        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user
        
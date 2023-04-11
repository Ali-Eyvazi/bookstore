"""
user manager
"""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    user manager (creating user)
    """

    def create_user(self, phone_number, email, full_name, password):
        """
        a method to create normal user
        """
        if not phone_number:
            raise ValueError('user must have phone number')
        if not email:
            raise ValueError('user must have an email')
        if not full_name:
            raise ValueError('user mus have a full name')
        user = self.model(phone_number=phone_number,
                          email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, full_name, password):
        """
        a method to create supperuser 
        """
        user = self.create_user(phone_number, email, full_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

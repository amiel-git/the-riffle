from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class ProfileManager(BaseUserManager):
    """
    Handles the creation of our profiles
    """
    def create_user(self,email,password=None,**kwargs):

        if not email:
            raise ValueError("Missing email address")

        email = self.normalize_email(email)
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self,email,password,**kwargs):
        user = self.create_user(email=email,password=password,**kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        return user


class Profile(AbstractBaseUser,PermissionsMixin):
    """
    Base user model that we are going to use
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    password = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'address'
    ]


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
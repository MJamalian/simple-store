from typing import Any
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email is required")

        user = User(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = User.UserRole.MANAGER
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    class UserRole(models.TextChoices):
        MANAGER = "manager"
        ASSISTANT = "assistant"
        STAFF = "staff"
        CUSTOMER = "customer"

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=15, choices=UserRole.choices, default=UserRole.CUSTOMER)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    objects = UserManager()

    USERNAME_FIELD = "email"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}, {self.stock}"
